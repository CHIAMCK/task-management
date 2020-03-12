import django_tables2 as tables

from ..models import TeamMember


class TeamMemberTable(tables.Table):

    name = tables.TemplateColumn(
        '''
        <a href="{% url 'team_members:edit' record.pk %}">
            {{record.name}}
        </a>
        ''',
        orderable=False
    )

    email = tables.Column(
        'Phone', orderable=False
    )



    class Meta():
        model = TeamMember
        # add custom HTML attributes to the table
        attrs = {'class': 'table table-striped table-responsive-sm'}
        fields = (
            'name', 'email'
        )
