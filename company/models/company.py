from django.db import models

from ..constants import status


class Company(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    status = models.SmallIntegerField(default=status.ACTIVE_INT, choices=status.STATUS_OPTIONS)
