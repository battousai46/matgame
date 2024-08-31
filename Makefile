install-dependencies:
	pip install poetry==1.8.3
	poetry install --only main


install_hooks:
	pre-commit install

make-migrations:
	poetry run python manage.py makemigrations

