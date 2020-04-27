from django.urls import re_path, path

import task.views

app_name = 'tasks'

urlpatterns = [
    path('add', task.views.AddTaskView.as_view(), name='add'),
    path('list', task.views.ListTaskView.as_view(), name='list'),
    path('edit/<int:pk>', task.views.EditTaskView.as_view(), name='edit'),
    path('delete/<int:pk>', task.views.DeleteTaskView.as_view(), name='delete'),
    re_path('add_task_activity_form/(?P<task_id>[\d]+)(?:/save_activity_(?P<activity_type>[\d]+))?', task.views.TaskActivityView.as_view(), name='task_activity'),
    path('list/<int:pk>', task.views.TaskActivityListView.as_view(), name='list_task_activity'),
]
