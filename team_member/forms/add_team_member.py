from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout


from utils.forms.layout import FormCard, SubmitButtons

from ..models import TeamMember

# create a class that inherit django form class
# form type, modelForm, normal form
# form validation


class AddTeamMemberForm(forms.ModelForm):

    class Meta:
        model = TeamMember
        fields = [
            'name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        fields = ['name', 'email']

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(css_class='col-sm-3 d-xs-none'),
                FormCard('Team Member details', fields, icon='queue'),
                css_class='row'
            ),
            Div(
                Div(css_class='col-sm-3 d-xs-none'),
                Div(SubmitButtons(), css_class='col-sm-6 col-xs-12'),
                css_class='row'
            )
        )

    def save(self, commit=True):

        default_password = 'Abcd123!'

        self.instance.company_id = self.request.user.team_member.company_id
        # create user
        # TODO send verfication email and reset password
        user = User.objects.create_user(
            username=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            password=default_password
        )
        # add user id to the team member instance
        self.instance.user_id = user.id
        return super().save(commit=commit)
