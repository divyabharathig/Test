#!/bin/bash
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py createsu --no-input

gunicorn portfolio.wsgi:application
