from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ..models import TeamMember
from ..forms import AddTeamMemberForm
from utils.views.forms import PassRequestToFormView

# using createview
# create form template
# create route


class AddTeamMemberView(PassRequestToFormView, CreateView):
    model = TeamMember
    form_class = AddTeamMemberForm
    template_name = 'team_member_form.html'
    success_url = reverse_lazy('dashboard:main')
