from django.db import models

from ..constants import status


class Task(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True, default='')

    status = models.SmallIntegerField(default=status.NEW_INT, choices=status.STATUS_OPTIONS)

    due_date = models.DateTimeField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now_add=True)

    deleted_date = models.DateTimeField(blank=True, null=True)

    company = models.ForeignKey(
        to='company.Company',
        on_delete=models.CASCADE,
        related_name='+'
    )

    assigned_to = models.ForeignKey(
        to='team_member.TeamMember',
        on_delete=models.CASCADE,
        related_name='+'
    )

    created_by = models.ForeignKey(
        to='team_member.TeamMember',
        on_delete=models.CASCADE,
        related_name='+'
    )

    updated_by = models.ForeignKey(
        to='team_member.TeamMember',
        on_delete=models.CASCADE,
        related_name='+'
    )

    deleted_by = models.ForeignKey(
        to='team_member.TeamMember',
        on_delete=models.CASCADE,
        related_name='+',
        null=True,
        blank=True
    )

    def get_status_color(self):
        return {
            status.NEW_INT: 'danger',
            status.IN_PROGRESS_INT: 'info',
            status.PENDING_INT: 'warning',
            status.COMPLETED_INT: 'success'
        }.get(self.status, 'danger')
