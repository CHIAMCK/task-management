from django.db import models

from utils.models import SoftDeleteModel
from .manager import Manager


class TeamMember(SoftDeleteModel, models.Model):

    def __str__(self):
        return self.name

    objects = Manager()

    user = models.OneToOneField(
        to='auth.User',
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='team_member'
    )

    name = models.CharField(max_length=200)

    email = models.EmailField()

    # created_date = models.DateTimeField(auto_now_add=True)

    deleted_date = models.DateTimeField(null=True, blank=True)

    company = models.ForeignKey(
        to='company.Company',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )
