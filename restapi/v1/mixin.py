from django.conf import settings
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # on each XMLHttpRequest, set a custom X-CSRFToken header
        # (as specified by the CSRF_HEADER_NAME setting) to the value of the
        # CSRF token.
        request.META[settings.CSRF_HEADER_NAME] = request.COOKIES.get('csrftoken', '')
        return super().enforce_csrf(request)
