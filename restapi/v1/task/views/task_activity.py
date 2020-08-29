from django.forms.models import model_to_dict

from rest_framework.status import HTTP_201_CREATED
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from task.models import Task
from task.forms import AddCommentForm, AddAttachmentForm, ChangeStatusForm
from task.constants.activity import ADD_COMMENT_INT, ADD_ATTACHMENT_INT, CHANGE_STATUS_INT

from ..serializers import TaskActivitySerializer


class TaskActivityListAddView(ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_date')
    serializer_class = TaskActivitySerializer

    def create(self, request, *args, **kwargs):
        task = self.get_object()
        kwargs = {
            'request': request,
            'data': request.data,
            'task_id': task.id,
            'files': request.FILES
        }

        form_classes = {
            ADD_COMMENT_INT: AddCommentForm,
            ADD_ATTACHMENT_INT: AddAttachmentForm,
            CHANGE_STATUS_INT: ChangeStatusForm,
        }

        activity_type = request.data['activity_type']
        form = form_classes[int(activity_type)](**kwargs)

        if form.is_valid():
            return_data = form.save()
            serializer = self.get_serializer(data=model_to_dict(return_data))
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response({'errors': form.errors},
                            status=HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        task = self.get_object()

        # Return a single page of results, or `None` if pagination is disabled.
        page = self.paginate_queryset(task.activities.order_by('-created_date'))
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(page, many=True)
        return Response(serializer.data)
