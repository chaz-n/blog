FROM nginx:alpine

COPY ./* /etc/nginx/
COPY ./run.sh /run.sh

USER root

RUN apk add --no-cache openssl bash

CMD ["/run.sh"]