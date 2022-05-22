#!/bin/bash

echo "Dependencies install"
poetry install

echo "Apply migrations"
poetry run python manage.py migrate

echo "Creating superuser"
poetry run python manage.py createsuperuser --noinput

echo "Server start up"
poetry run python manage.py runserver  0.0.0.0:$PORT
