from django.views.generic.edit import FormView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from utils.views import RestrictTaskListMixin

from ..filters import TaskFilter
from ..forms import AddAttachmentForm, AddCommentForm
from ..models import Task
from ..tables import TaskTable


class ListTaskView(SingleTableMixin, RestrictTaskListMixin, FilterView):
    model = Task
    template_name = 'task_list.html'

    # django table
    table_class = TaskTable

    # django filter
    filterset_class = TaskFilter


class TaskActivityView(FormView):
    template_name = 'task_activity.html'

    def get_context_data(self, form=None):
        context = super().get_context_data(form=form)
        context['forms'] = {
            x: C()
            for x, C in (
                ('comment', AddCommentForm),
                ('attachment', AddAttachmentForm),
            )
        }
        return context
