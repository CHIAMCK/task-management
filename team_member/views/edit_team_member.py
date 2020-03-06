from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from ..models import TeamMember
from ..forms import EditTeamMemberForm
from utils.views.forms import PassRequestToFormView

# using createview
# create form template
# create route


class EditTeamMemberView(PassRequestToFormView, UpdateView):
    model = TeamMember
    form_class = EditTeamMemberForm
    template_name = 'team_member_edit.html'
    success_url = reverse_lazy('team_members:list')
