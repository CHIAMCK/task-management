import django_tables2 as tables

from ..models import Task


class TaskTable(tables.Table):
    title = tables.Column(
        'Ttile', orderable=False
    )

    status = tables.Column(
        'Status', orderable=False
    )

    assigned_to = tables.Column(
        'Assigned to', orderable=False
    )

    created_on = tables.Column(
        'Created on', orderable=False
    )

    #  global settings for table
    class Meta():
        model = Task
        # add custom HTML attributes to the table
        attrs = {'class': 'table table-striped table-responsive-sm'}
        fields = (
            'title', 'status', 'assigned_to', 'created_on'
        )
