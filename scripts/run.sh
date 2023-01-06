#!/bin/sh

set -e

# Script for execution in deployment

python manage.py collectstatic --noinput

# uwsgi --socket :9000 --master --enable-threads --module app.wsgi

uwsgi --socket :9000 --workers  --master --enable-threads --module app.wsgi