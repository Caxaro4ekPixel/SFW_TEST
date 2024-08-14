#!/usr/bin/env bash

set -e

until python manage.py migrate --plan > /dev/null 2>&1; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."

python manage.py makemigrations
python manage.py migrate

python manage.py seed

echo "Testing contract 32812" >&2 && python manage.py test_contract --id 32812

exec "$@"
