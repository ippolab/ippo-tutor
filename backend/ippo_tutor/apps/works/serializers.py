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
        fields = '__all__'
