from django.core.validators import FileExtensionValidator

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    zip_with_templates = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    class Meta:
        model = Task
        fields = '__all__'
