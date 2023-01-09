FROM nginx:alpine

COPY ./nginx/* /etc/nginx/
COPY ./run.sh /run.sh

USER root

RUN apk add --no-cache openssl bash

CMD ["/run.sh"]