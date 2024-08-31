#!/bin/sh

set -e

orig=$*
cmd=$1
shift

if [ "$cmd" = 'web-local' ]; then
  python manage.py migrate
  python manage.py collectstatic --no-input
  exec gunicorn matgame.wsgi -c gunicorn.py --reload
elif [ "$cmd" = 'web' ]; then
  python manage.py collectstatic --no-input
  exec gunicorn matgame.wsgi -c gunicorn.py
elif [ "$cmd" = 'test' ]; then
  exec pytest -n auto
fi

exec $orig
