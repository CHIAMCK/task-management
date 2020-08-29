from rest_framework import serializers

from task.models import Task, TaskActivity


class TaskSerializer(serializers.ModelSerializer):
    # create a Serializer class with fields that correspond to the Model fields
    # allow complex data such as querysets and model instances to be converted to
    # native Python datatypes that can then be easily rendered into JSON, XML.
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'assigned_to')
        # serializer field arguments
        # extra_kwargs = {'description': {'allow_null': True}}

        # custom field level validation
        # def validate_title(self, value):

    # SerializerMethodField
    # This is a read-only field. It gets its value by calling a method on the serializer class it is attached to.


class TaskActivitySerializer(serializers.ModelSerializer):
    # get user name instead user id
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TaskActivity
        fields = ('note', 'activity_type', 'user', 'created_date')
