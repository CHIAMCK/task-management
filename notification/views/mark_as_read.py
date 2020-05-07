from django.http import JsonResponse
from django.views.generic import View


class MarkAsReadView(View):

    def post(self, request):
        user = request.user
        user.notifications.mark_all_as_read()
        return JsonResponse({'status': 200})
