from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout

from ..models import Task
from utils.forms.layout import FormCard, EditSubmitButtons


class EditTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'due_date',
            'assigned_to',
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        fields = ['title', 'description', 'status', 'due_date', 'assigned_to']

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(css_class='col-sm-3 d-xs-none'),
                FormCard('Task details', fields, icon='queue'),
                css_class='row'
            ),
            Div(
                Div(css_class='col-sm-3 d-xs-none'),
                Div(EditSubmitButtons(), css_class='col-sm-6 col-xs-12'),
                css_class='row'
            )
        )

    def save(self, commit=True):
        # want to autofill company, created_by, updated_by
        # fill these fields with the current user id
        # need to pass request obejct to the form, access user data, self.request.user
        # get the instance, set the value, instance.created_by_id = self.request.user.pk

        instance = super().save(commit=False)
        instance.updated_by_id = self.request.user.pk
        return super().save(commit=True)
