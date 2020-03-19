from django.urls import reverse_lazy
from django.views.generic import UpdateView

from utils.views.forms import PassRequestToFormView

from ..forms import EditTaskForm
from ..models import Task


class EditTaskView(PassRequestToFormView, UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'edit_task.html'
    success_url = reverse_lazy('tasks:list')
    prefix = 'tasks'
