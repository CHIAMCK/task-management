from django.db import models

from utils.models import SoftDeleteManager


class Manager(SoftDeleteManager, models.Manager):
    pass
