from django.db import models

from task.validator import validate_file_extension


class TaskAttachment(models.Model):
    file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        max_length=255,
        blank=True,
        null=True,
        validators=[validate_file_extension]
    )

    task_activity = models.ForeignKey(
        'task.TaskActivity',
        on_delete=models.CASCADE,
        related_name='attachments'
    )

    created_date = models.DateTimeField(blank=True, auto_now_add=True)
