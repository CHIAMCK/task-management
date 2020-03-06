# How to setup docker
- create a folder called docker, create docker-compose and Dockerfile
- export COMPOSE_FILE=./docker/docker-compose.yml


# How to setup webpack
- use django-webpack-loader
- set the STATICFILES_DIRS in settings.py
- create webpack.config.js
- add WEBPACK_LOADER in settings.py
- add webpack_loader to INSTALLED_APPS
- render the webpack bundle on master template
