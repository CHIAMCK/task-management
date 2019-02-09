import allauth.account.forms


class OverrideLoginForm(allauth.account.forms.LoginForm):
    def __init__(self, *args, **kwargs):
        super(OverrideLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False
