from django.db import models

from ..constants import activity


class TaskActivity(models.Model):

    task = models.ForeignKey(
        'task.Task',
        on_delete=models.CASCADE,
        related_name='activities'
    )

    note = models.TextField(blank=True, default='')

    activity_type = models.SmallIntegerField(
        help_text='Type of activity',
        choices=activity.ACTIVITY_OPTION
    )

    user = models.ForeignKey(
        'team_member.TeamMember',
        on_delete=models.CASCADE,
        related_name='activities'
    )

    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    details = models.TextField(default='', blank=True)


# click on a button
# render task activity form on modal
#


# backend
# create View using FormView
# create form class for each activity (comment, attachment, status)

# frontend
# create modal
# render form on modal
