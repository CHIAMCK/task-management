from django.urls import path, re_path

from .v1.authentication.views import LoginView, LogoutView
from .v1.task.manage_view import TaskManageView


urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    re_path('tasks(?:/(?P<pk>[\d]+|))?', TaskManageView.as_view()),
]
