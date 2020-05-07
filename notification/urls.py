from django.urls import path

import notification.views

app_name = 'notifications'

urlpatterns = [
    path('list', notification.views.ListNotificationView.as_view(), name='list'),
    path('mark_read', notification.views.MarkAsReadView.as_view(), name='mark_read'),
]
