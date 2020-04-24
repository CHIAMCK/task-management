from django.contrib import admin

from .models import Task, TaskActivity

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskActivity)
