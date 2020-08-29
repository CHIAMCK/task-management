import django_tables2 as tables

from ..models import Task


class TaskTable(tables.Table):
    task_number = tables.TemplateColumn(
        'Task number',
        orderable=False
    )

    title = tables.TemplateColumn(
        '''
        <a href="{% url 'tasks:detail' record.pk %}">
            {{record.title}}
        </a>
        ''',
        orderable=False,
        attrs={'th': {'width': '400'}}
    )

    status = tables.TemplateColumn(
        '''
        <span class="badge badge-{{record.get_status_color}}">
            {{record.get_status_display}}
        </span>
        ''',
        orderable=False
    )

    assigned_to = tables.Column(
        'Assigned to', orderable=False
    )

    created_date = tables.Column(
        'Created on', orderable=False
    )

    # action = tables.TemplateColumn(
    #     '''
    #     <a href="#"
    #        data-toggle="modal"
    #        data-target="#add-task-activity-modal"
    #        id="add-task-activity-button"
    #     >
    #         <i  data-task-id= {{ record.pk }}
    #             style="color:#4F8DED;
    #             font-size: 55px;
    #             width: 55px"
    #             class="material-icons align-middle">
    #             add_circle
    #         </i>
    #     </a>
    #     ''',
    #     orderable=False
    # )

    action_menu = tables.TemplateColumn(
        '''
        {% include 'partials/task_action_menu.html' with task=record %}

        ''',
        orderable=False
    )

    #  global settings for table
    class Meta():
        model = Task
        # add custom HTML attributes to the table
        attrs = {'class': 'table table-striped table-responsive-sm'}
        fields = (
            'task_number', 'title', 'status', 'assigned_to', 'created_date'
        )
