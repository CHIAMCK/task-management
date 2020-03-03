from django.urls import path
import team_member.views

app_name = 'team_members'

urlpatterns = [
    path('add', team_member.views.AddTeamMemberView.as_view(), name='add'),
]
