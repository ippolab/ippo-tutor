from rest_framework import serializers
from django.core.validators import FileExtensionValidator

from .models import Subject, SubjectType, Work


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = ('name',)


class WorkSerializer(serializers.ModelSerializer):
    file = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'zip'])])

    class Meta:
        model = Work
        fields = '__all__'
