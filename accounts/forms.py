import allauth.account.forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout
from django import forms


class OverrideLoginForm(allauth.account.forms.LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["some-field"] = forms.CharField(label='Some label', max_length=100)
        # Hide the label
        self.helper = FormHelper()
        print(self.helper.form_show_labels)
        self.helper.form_show_labels = False
        print(self.helper.form_show_labels)
        self.fields['password'].label = False
        
