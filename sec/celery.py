import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sec.settings')

app = Celery('sec')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# https://realpython.com/asynchronous-tasks-with-django-and-celery/
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django
# https://github.com/williln/celery-docker-example/blob/master/docker-compose.yml
