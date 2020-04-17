from django import forms


class AddCommentForm(forms.Form):
    comment = forms.CharField(label='Your comment', widget=forms.Textarea)


class AddAttachmentForm(forms.Form):
    attachment = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'accept': 'image/*, .doc, .docx, .pdf, .xlsx, .xls, .zip'
        })
    )
