from django.views.generic import ListView
from django_tables2.views import SingleTableMixin

from ..models import TeamMember
from ..tables import TeamMemberTable


class ListTeamMemberView(SingleTableMixin, ListView):
    # ListView
    model = TeamMember
    template_name = 'team_member_list.html'

    # django table
    table_class = TeamMemberTable
