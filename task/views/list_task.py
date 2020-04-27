from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, FormView
from django_filters.views import FilterView

from django_tables2.views import SingleTableMixin
from django.shortcuts import reverse

from utils.views import RestrictTaskListMixin

from ..constants.activity import (ADD_COMMENT_INT, ADD_ATTACHMENT_INT, CHANGE_STATUS_INT)
from ..filters import TaskFilter
from ..forms import AddAttachmentForm, AddCommentForm, ChangeStatusForm
from ..models import Task
from ..tables import TaskTable


class ListTaskView(SingleTableMixin, RestrictTaskListMixin, FilterView):
    model = Task
    template_name = 'task_list.html'

    # django table
    table_class = TaskTable

    # django filter
    filterset_class = TaskFilter


class TaskActivityListView(DetailView):
    model = Task
    template_name = 'task_activity_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = self.object.activities.order_by('-created_date')
        return context


class TaskActivityView(SuccessMessageMixin, FormView):
    success_message = 'Activity recorded'
    template_name = 'task_activity.html'
    form_classes = {
        ADD_COMMENT_INT: AddCommentForm,
        ADD_ATTACHMENT_INT: AddAttachmentForm,
        CHANGE_STATUS_INT: ChangeStatusForm,
    }

    def get_success_url(self):
        return reverse('tasks:task_activity', args=(self.kwargs['task_id'],))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # pass kwargs to form class
        kwargs['task_id'] = self.kwargs['task_id']
        kwargs['request'] = self.request
        return kwargs

    def get_form_class(self):
        # select which form to process based on activity_type
        # can access data on url using self.kwargs['']
        return self.form_classes[int(self.kwargs['activity_type'])]

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # call the save method in form
        form.save()
        return super().form_valid(form)

    def get_context_data(self, form=None):
        context = super().get_context_data(form=form)
        context['forms'] = {
            x: C(**self.get_form_kwargs())
            for x, C in (
                ('comment', AddCommentForm),
                ('attachment', AddAttachmentForm),
                ('status', ChangeStatusForm),
            )
        }
        return context
