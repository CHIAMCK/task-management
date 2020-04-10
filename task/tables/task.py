import django_tables2 as tables

from ..models import Task


class TaskTable(tables.Table):
    task_number = tables.TemplateColumn(
        'Task number',
        orderable=False
    )

    title = tables.TemplateColumn(
        '''
        <a href="{% url 'tasks:edit' record.pk %}">
            {{record.title}}
        </a>
        ''',
        orderable=False,
        attrs={'th': {'width': '400'}}
    )

    status = tables.Column(
        'Status', orderable=False
    )

    assigned_to = tables.Column(
        'Assigned to', orderable=False
    )

    created_date = tables.Column(
        'Created on', orderable=False
    )

    #  global settings for table
    class Meta():
        model = Task
        # add custom HTML attributes to the table
        attrs = {'class': 'table table-striped table-responsive-sm'}
        fields = (
            'task_number', 'title', 'status', 'assigned_to', 'created_date'
        )
