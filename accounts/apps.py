# from django.apps import AppConfig
# from django.contrib.auth.signals import user_logged_in



# def add_company_to_session(sender, request, user, **_):
#     try:
#         request.session.__setitem__('company_id', user.team_member.company_id)
#     except ():


# class AccountsConfig(AppConfig):
#     name = 'accounts'

    # override this method to perform initialization tasks such as registering signals.
    # To receive a signal, register a receiver function using the Signal.connect() method.
    # The receiver function is called when the signal is sent.
    # def ready(self, *args, **kwargs):
    #     user_logged_in.connect()
    #     user_logged_in.connect()
