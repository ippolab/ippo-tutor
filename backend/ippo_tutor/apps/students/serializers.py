from rest_framework import serializers

from .models import StudentProfile


class StudentProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = StudentProfile
        fields = ('username', 'first_name', 'second_name', 'last_name',)