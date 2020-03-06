from django.urls import path

import team_member.views

app_name = 'team_members'

urlpatterns = [
    path('add', team_member.views.AddTeamMemberView.as_view(), name='add'),
    path('list', team_member.views.ListTeamMemberView.as_view(), name='list'),
    path('edit/<int:pk>', team_member.views.EditTeamMemberView.as_view(), name='edit'),
    path('delete/<int:pk>', team_member.views.DeleteTeamMemberView.as_view(), name='delete')
]
