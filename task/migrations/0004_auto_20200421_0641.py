# Generated by Django 2.1.5 on 2020-04-21 06:41

from django.db import migrations, models
import django.db.models.deletion
import task.validator


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20200420_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, max_length=255, null=True, upload_to='uploads/%Y/%m/%d/', validators=[task.validator.validate_file_extension])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='taskactivity',
            name='activity_type',
            field=models.SmallIntegerField(choices=[(1, 'Add Comment'), (2, 'Add Attachment'), (3, 'Change status')], help_text='Type of activity'),
        ),
        migrations.AddField(
            model_name='taskattachment',
            name='task_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='task.TaskActivity'),
        ),
    ]
