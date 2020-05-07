from restapi.v1.task.views import TaskAddView, TaskListView
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseManagerView(APIView):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception('VIEWS_BY_METHOD is not found')
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method]()(request, *args, **kwargs)
        return Response(status=405)


class TaskManageView(BaseManagerView):
    # using different views for different http methods
    VIEWS_BY_METHOD = {
        'POST': TaskAddView.as_view,
        'GET': TaskListView.as_view,
    }
