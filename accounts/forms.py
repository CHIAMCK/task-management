import allauth.account.forms
from crispy_forms.helper import FormHelper


class OverrideLoginForm(allauth.account.forms.LoginForm):

    def __init__(self, *args, **kwargs):
        super(OverrideLoginForm, self).__init__(*args, **kwargs)

        # Hide the label
        self.helper = FormHelper()
        self.helper.form_show_labels = False
