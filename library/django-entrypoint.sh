#!/bin/bash

sleep 5
export PYTHONIOENCODING=UTF-8
export PYTHONUNBUFFERED=1

# python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000