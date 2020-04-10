from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from utils.views import RestrictTaskListMixin

from ..filters import TaskFilter
from ..models import Task
from ..tables import TaskTable


class ListTaskView(SingleTableMixin, RestrictTaskListMixin, FilterView):
    model = Task
    template_name = 'task_list.html'

    # django table
    table_class = TaskTable

    # django filter
    filterset_class = TaskFilter
