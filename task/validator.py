import os

from django.core.exceptions import ValidationError


def validate_file_extension(value):
    file_size = value.file_size
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls', '.zip']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    elif file_size > 2*1024*1000:
        raise ValidationError('Maximum file size is 2MB')
