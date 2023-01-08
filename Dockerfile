FROM python:3.10-alpine3.16

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY mysite/ /mysite
WORKDIR /mysite

COPY scripts/run.sh /run.sh
RUN chmod +x /run.sh

RUN adduser --disabled-password --no-create-home django
RUN chown -R django:django /mysite

USER django

RUN python manage.py collectstaic
CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "mysite.wsgi"]
