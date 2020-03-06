from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from ..models import TeamMember

# need to override the delete() of model
# add deleted_date (soft delete)


class DeleteTeamMemberView(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('team_members:list')
