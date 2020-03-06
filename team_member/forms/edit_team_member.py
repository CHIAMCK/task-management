from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout

from utils.forms.layout import FormCard, EditSubmitButtons

from ..models import TeamMember


class EditTeamMemberForm(forms.ModelForm):

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
                Div(EditSubmitButtons(), css_class='col-sm-6 col-xs-12'),
                css_class='row'
            )
        )

    def save(self, commit=True):
        self.instance.company_id = self.request.user.team_member.company_id
        return super().save(commit=commit)
