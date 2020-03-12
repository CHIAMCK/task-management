from django.urls import path

import task.views

app_name = 'tasks'

urlpatterns = [
    path('add', task.views.AddTaskView.as_view(), name='add'),
    path('list', task.views.ListTaskView.as_view(), name='list'),
]
