# `python-base` sets up all our shared environment variables
FROM python:3.11-slim as python-base

    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.8.3 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        libpq-dev \
        librdkafka-dev


# `builder-base` stage is used to build deps + create our virtual environment
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential \
        gcc \
        openssh-client \
        git

# set up private repo access
ARG GITHUB_TOKEN
RUN git config --global url."https://${GITHUB_TOKEN}@github.com/battousai46/".insteadOf "git@github.com:battousai46/"

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./


# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
# TODO: RUN poetry install --only main
RUN poetry install


# `development` image is used during development / testing
FROM python-base as development
ENV ENVIRONMENT=development
WORKDIR $PYSETUP_PATH

# copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# quicker install as runtime deps are already installed
RUN poetry install

# will become mountpoint of our code
WORKDIR /app

EXPOSE 8000
ENTRYPOINT ["./entry.sh"]
CMD ["web"]


# `poc` image used for runtime
FROM python-base as poc
ENV ENVIRONMENT=poc

# copy in our built venv
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# set up non-root user, numerics done manually so that charts don't complain.
RUN addgroup --gid 1000 webapp
RUN adduser -u 1000 --gid 1000 webapp
USER webapp

COPY --chown=webapp:webapp . /app/
WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["./entry.sh"]
CMD ["web"]
