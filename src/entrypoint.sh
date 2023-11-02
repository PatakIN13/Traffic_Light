#!/bin/sh

python manage.py flush --no-input
python manage.py migrate
python manage.py load_position
python manage.py load_department
python manage.py load_data
python manage.py initadmin

exec "$@"
