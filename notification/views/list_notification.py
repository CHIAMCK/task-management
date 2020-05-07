from django.views.generic import ListView

from notifications.models import Notification
from utils.views.forms import PassRequestToFormView


class ListNotificationView(ListView):
    model = Notification
    template_name = 'list_notification.html'
    context_object_name = 'notifications'
