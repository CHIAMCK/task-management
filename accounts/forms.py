import allauth.account.forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout
from django import forms


class OverrideLoginForm(allauth.account.forms.LoginForm):

    def __init__(self, *args, **kwargs):
        super(OverrideLoginForm, self).__init__(*args, **kwargs)
        
        # Hide the label
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['login'].label = False
        self.fields['password'].label = False
        