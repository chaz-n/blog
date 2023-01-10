# Charlie Django Site

This is a personal blog / potential portfolio website built using the Python Django framework.

## Front-end:
* Bootstrap 5.3

## Current features:
* Django user system with frontend access/management
* Profile system linked with user system, with profile pictures and frontend to modify profile
* SQLite database with a model for the blog posts system
* Search and pagination
* Frontend to create, update and delete posts from database
* Integration with the Summernote WYSIWYG text editor for post creation

## Planned features:
* ### Not a clue

<br>

## Deployment:
* PostgresSQL is used for the production database
* Gunicorn is used as the production WSGI server
* Nginx acts as a reverse proxy for gunicorn
* Certbot is used to grab and renew Let's Encrypt SSL certificates

These instructions assume that a VPS has been set up, with a domain pointing at its public IPv4 
and that docker and docker compose has been installed.

The GitHub repository needs to be pulled to the remote server. Then create a <code>.env</code> from the <code>.env.sample</code> file:

    cp .env.sample .env

Adjust the environment variables in <code>.env</code>:
    
    DEBUG=0                 # Sets DEBUG mode in Django, leave as 0 in production
    SECRET_KEY=change_me    # a secret Django key can be generated using get_random_secret_key() in Django shell
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=postgres
    SQL_USER=postgres
    SQL_PASSWORD=test
    SQL_HOST=db
    SQL_PORT=5432
    DATABASE=postgres
    POSTGRES_PASSWORD=test
    ACME_DEFAULT_EMAIL=email@example.com    # set your email address
    DOMAIN=localhost                        # set to your domain name

Ensure that the latest version of the docker containers has been built:

    docker-compose -f docker-compose-deploy.yml build

Grab the initial Let's Encrypt SSL certificates for your domain using certbot:

    docker-compose -f docker-compose-deploy.yml run --rm certbot /opt/certify-init.sh

Then tear down all the containers:

    docker-compose -f docker-compose-deploy.yml down

Then start them up again in detached mode:
    
    docker-compose -f docker-compose-deploy.yml up -d

### Automatic SSL certificate renewal
Let's Encrypt certificates only last 3 months, therefore they need to be renewed every so often. This 
can be done with this command:

    docker-compose -f docker-compose-deploy.yml run --rm certbot sh -c "certbot renew"

To automate this, create a <code>renew_ssl.sh</code> file in your users home directory with this content:

    #!/bin/sh
    set -e
    
    cd /home/(your user)/blog

    docker-compose -f docker-compose-deploy.yml run --rm certbot certbot renew

Then make it executable with <code>chmod +x renew_ssl.sh</code>

This can than be added to the server's crontab <code>crontab -e</code>, the follow entry will renew the SSL
certificates at 00:00 every Saturday:

    0 0 * * 6 sh /home/(your user)/blog_renew_ssl.sh
