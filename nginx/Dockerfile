FROM nginx:alpine

COPY ./proxy/* /etc/nginx/
COPY ./run.sh /run.sh


USER root

RUN apk add --no-cache openssl bash
RUN chmod +x /run.sh

CMD ["/run.sh"]