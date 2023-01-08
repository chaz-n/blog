FROM python:alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY mysite/ /mysite
WORKDIR mysite
RUN mkdir -p static_files
RUN mkdir -p media_files


COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]