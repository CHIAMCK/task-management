from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from ..mixin import CsrfExemptSessionAuthentication


class LoginView(APIView):
    # subclasses Dajgno's View class
    # using REST framewrok's Request, Response instance
    # set the authentication schme on a per-view basis
    authentication_classes = []
    # set the authorization policy on a per-view basis
    permission_classes = []

    @csrf_exempt
    def post(self, request):
        return self.login_user(request)

    def login_user(self, request):
        # get the data from request instance
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    def post(self, request):
        return self.logout_user(request)

    def logout_user(self, request):
        logout(request)
        return Response(status=HTTP_200_OK)
