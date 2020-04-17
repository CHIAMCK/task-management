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

    action = tables.TemplateColumn(
        '''
        <a href="#"
           data-toggle="modal"
           data-target="#add-task-activity-modal"
           id="add-task-activity-button"
        >
        <i style="color:#3BF944; font-size: 55px; width: 55px" class="material-icons align-middle">add_circle</i>
        </a>
        ''',
        orderable=False
    )

    #  global settings for table
    class Meta():
        model = Task
        # add custom HTML attributes to the table
        attrs = {'class': 'table table-striped table-responsive-sm'}
        fields = (
            'task_number', 'title', 'status', 'assigned_to', 'created_date',
            'action'
        )
