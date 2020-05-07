from rest_framework.generics import ListAPIView

from task.models import Task
from utils.views import RestrictTaskListMixin

from ..serializers import TaskSerializer


class TaskListView(RestrictTaskListMixin, ListAPIView):
    queryset = Task.objects.all().order_by('-created_date')
    serializer_class = TaskSerializer

    # override get queryset method to return tasks that are assigned to the user
