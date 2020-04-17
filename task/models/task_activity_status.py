from django.db import models

from task.constants import status


class TaskActivityStatus(models.Model):

    task_activity = models.OneToOneField(
        'task.TaskActivity',
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='task_activity_status'
    )

    status_before = models.SmallIntegerField(
        choices=status.STATUS_OPTIONS,
        db_index=True
    )

    status_after = models.SmallIntegerField(
        choice=status.STATUS_OPTIONS,
        db_index=True
    )

    created_date = models.DateTimeField(blank=True, auto_now_add=True)
