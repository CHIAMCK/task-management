from django.urls import reverse_lazy
from django.views.generic import CreateView

from utils.views.forms import PassRequestToFormView

from ..forms import AddTaskForm
from ..models import Task


class AddTaskView(PassRequestToFormView, CreateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'add_task_form.html'
    success_url = reverse_lazy('tasks:list')
    suffix = 'tasks'
