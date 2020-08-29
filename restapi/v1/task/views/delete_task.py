from django.utils import timezone

from rest_framework.generics import DestroyAPIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from task.models import Task
from ..serializers import TaskSerializer


class TaskDeleteView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def delete(self, request, *args, **kwargs):
        soft_delete_field = 'deleted_date'
        instance = self.get_object()
        setattr(instance, soft_delete_field, timezone.now())
        instance.save()
        return Response(status=HTTP_200_OK)
