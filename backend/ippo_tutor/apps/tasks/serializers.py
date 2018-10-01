from django.core.validators import FileExtensionValidator

from rest_framework import serializers

from .models import Task, Subject, SubjectType


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ('id',)


class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = '__all__'
        read_only_fields = ('id',)


class TaskSerializer(serializers.ModelSerializer):
    zip_with_templates = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id',)
