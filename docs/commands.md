# How to create virtualenv

- mkvirtualenv projectx -p /usr/bin/python3.6

- lsvirtualenv

- rmvirtualenv <virtualenv_name>


# How to create database
- docker-compose exec db /bin/bash

- mysql -h db -u root -p # the password refer to DATABASES in settings.py

- mysql> create database your_database_name;

# Migration
`$ docker-compose exec web python manage.py migrate`

# Create superuse
`$ docker-compose exec web python manage.py createsuperuser`
