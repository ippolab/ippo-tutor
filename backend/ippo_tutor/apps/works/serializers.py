from rest_framework import serializers

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
    file = serializers.FileField()

    class Meta:
        model = Work
        fields = (
            'title',
            'status',
            'file',
            'loaded',
            'checked',
            'subject',
            'subject_type',
            'student',
            'tutor',
        )
