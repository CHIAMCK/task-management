from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from utils.views import RestrictTaskListMixin

from ..models import TeamMember
from ..tables import TeamMemberTable
from ..filters import TeamMemberFilter


class ListTeamMemberView(SingleTableMixin, RestrictTaskListMixin, FilterView):
    # ListView
    model = TeamMember
    template_name = 'team_member_list.html'

    # django table
    table_class = TeamMemberTable

    # django filter
    filterset_class = TeamMemberFilter
