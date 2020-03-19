from django.urls import reverse_lazy
from django.views.generic import DeleteView

from ..models import Task


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')
