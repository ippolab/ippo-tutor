from rest_framework import serializers

from .models import StudentProfile, Group


class StudentProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    group = serializers.CharField(source='group.name', allow_null=True)

    class Meta:
        model = StudentProfile
        fields = ('username', 'first_name', 'second_name', 'last_name', 'group',)

    def update(self, instance, validated_data):
        group = validated_data.pop('group')
        instance = super().update(instance, validated_data)
        instance.group, _ = Group.objects.get_or_create(name=group['name'])
        instance.save()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    students = StudentProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('name', 'students',)
