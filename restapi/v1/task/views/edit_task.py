from django.forms.models import model_to_dict

from rest_framework.generics import UpdateAPIView
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from task.models import Task
from task.forms import EditTaskForm

from ..serializers import TaskSerializer


class TaskEditView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        kwargs = {
            'request': request,
            'data': request.data,
            'instance': instance
        }

        model_form = EditTaskForm(**kwargs)
        if model_form.is_valid():
            return_data = model_form.save()
            serializer = self.get_serializer(data=model_to_dict(return_data))
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response({'errors': model_form.errors},
                            status=HTTP_400_BAD_REQUEST)
