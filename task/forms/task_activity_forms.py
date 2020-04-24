import json

from django import forms
from django.urls import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit

from ..constants import activity, status
from ..models import Task, TaskActivity, TaskAttachment, TaskActivityStatus


class AddTaskActivityForm(forms.Form):
    def __init__(self, task_id, request, **kwargs):
        self.task_id = task_id
        self.request = request
        super().__init__(**kwargs)
        self.helper = FormHelper()
        # add form action
        self.helper.form_action = self.get_action()
        # add form button
        self.helper.add_input(
            Submit('save', 'Save', css_class='btn btn-success')
        )
        self.helper.add_input(
            Button('cancel', 'Cancel', data_dismiss='modal', css_class='btn btn-link')
        )

    def get_action(self):
        return reverse('tasks:task_activity', kwargs={
            'task_id': self.task_id,
            'activity_type': self.activity_type
        })


class AddCommentForm(AddTaskActivityForm):
    activity_type = activity.ADD_COMMENT_INT
    comment = forms.CharField(label='Your comment', widget=forms.Textarea)

    def save(self, *args, **kwargs):
        # get the form data from self.cleaned_data[]
        comment = self.cleaned_data['comment']
        note = f'{self.request.user.team_member} added comment: "{comment}"'

        return TaskActivity.objects.create(
            note=note,
            task_id=self.task_id,
            activity_type=self.activity_type,
            user=self.request.user.team_member,
            details=json.dumps({
                'user': self.request.user.id,
                'type': self.activity_type,
                'comment': comment
            })
        )


class AddAttachmentForm(AddTaskActivityForm):
    activity_type = activity.ADD_ATTACHMENT_INT
    attachment = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'accept': 'image/*, .doc, .docx, .pdf, .xlsx, .xls, .zip'
        })
    )

    def save(self, *args, **kwargs):
        file = self.request.FILES['attachment']
        file_name = file.name
        print(file_name)
        note = f'{self.request.user.team_member} uploaded {file_name}'

        activity = TaskActivity.objects.create(
            note=note,
            task_id=self.task_id,
            activity_type=self.activity_type,
            user=self.request.user.team_member,
            details=json.dumps({
                'user': self.request.user.id,
                'type': self.activity_type,
                'file': file_name
            })
        )

        TaskAttachment.objects.create(
            file=file,
            task_activity=activity
        )

        return activity


class ChangeStatusForm(AddTaskActivityForm):
    activity_type = activity.CHANGE_STATUS_INT
    status = forms.ChoiceField(label='Status', choices=status.STATUS_OPTIONS)

    def save(self, *args, **kwargs):
        new_status = int(self.cleaned_data['status'])
        current_task = Task.objects.get(id=self.task_id)
        current_status = current_task.id
        note = f'{self.request.user.team_member} changed the status to {status.STATUS_OPTIONS_DICT[new_status]}.'

        activity = TaskActivity.objects.create(
            note=note,
            task_id=self.task_id,
            activity_type=self.activity_type,
            user=self.request.user.team_member,
            details=json.dumps({
                'user': self.request.user.id,
                'type': self.activity_type,
                'status_before': current_status,
                'status_after': new_status
            })
        )

        current_task.status = new_status
        current_task.save()

        TaskActivityStatus.objects.create(
            task_activity=activity,
            status_before=current_status,
            status_after=new_status,
        )

        return activity
