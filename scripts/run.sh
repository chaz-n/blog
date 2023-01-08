#!/bin/bash

python manage.py collectstaic  --noinput

uwsgi --socket :9000 --workers  --master --enable-threads --module mysite.wsgi