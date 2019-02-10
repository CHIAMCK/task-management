from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/"
        if request.user.is_authenticated:
            path = reverse('dashboard:main')  # example-html  # my-profile
        else:
            path = reverse('example-plain')
        return path.format(username=request.user.username)    
