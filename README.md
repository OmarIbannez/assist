# Assist

Download project
=====================

    $ git clonehttps://github.com/OmarIbannez/assist.git

Installing virtualenv
=====================

    $ sudo apt-get install python-virtualenv

Installing nginx
=====================

    $ sudo apt-get install nginx

Installing postgresql
=====================

    $ sudo apt-get install libpq-dev python-dev
    $ sudo apt-get install postgresql postgresql-contrib


Creating virtualenv
=====================

    $ virtualenv venv

Installing dependencies
=====================

    $ source venv/bin/activate
    $ pip install -r requirements/requirements.txt




Creating DB
=====================

    $ sudo -i -u postgres
    $ createdb databasename
    $ psql
    $ CREATE USER username WITH PASSWORD 'password';
    $ GRANT ALL PRIVILEGES ON DATABASE databasename to username;


Migrating models
=====================
python manage.py migrate


Create first username
=====================
python manage.py createsuperuser


Run project (only for test)
=====================
python manage.py runserver
