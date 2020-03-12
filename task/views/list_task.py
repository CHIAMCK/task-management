from django.views.generic import ListView
from django_tables2.views import SingleTableMixin

from ..models import Task
from ..tables import TaskTable


class ListTaskView(SingleTableMixin, ListView):
    model = Task
    template_name = 'task_list.html'

    # django table
    table_class = TaskTable
