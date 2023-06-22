#!/bin/bash
set -e

pip install --no-cache-dir -r /app/requirements.txt
# python /app/manage.py startapp products
# python /app/manage.py makemigrations products
# python /app/manage.py createsuperuser
python /app/manage.py migrate
python /app/manage.py runserver 0.0.0.0:8000
