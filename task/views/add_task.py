from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from utils.views.forms import PassRequestToFormView
from notification.task import send_notification

from ..forms import AddTaskForm
from ..models import Task


class AddTaskView(PassRequestToFormView, CreateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'add_task_form.html'
    success_message = 'Task created'
    success_url = reverse_lazy('tasks:list')
    suffix = 'tasks'

    def form_valid(self, form):
        task = form.save()
        # send to team member that is assigned to the task
        # don't send to creator
        recipient = task.assigned_to.user.pk
        url = reverse('tasks:edit', kwargs={'pk': task.id})
        title = task.title
        formatted_task = f'<a href="{url}">{title}</a>'
        verb = f'{self.request.user.team_member.name} created task {formatted_task}'

        send_notification.delay(self.request.user.pk, recipient, verb)
        return super().form_valid(form)
