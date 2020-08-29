from django.views.generic import DetailView

from utils.views.forms import PassRequestToFormView

from ..models import Task


class DetailTaskView(PassRequestToFormView, DetailView):
    model = Task
