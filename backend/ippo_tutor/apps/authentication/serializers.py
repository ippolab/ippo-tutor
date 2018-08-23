from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=4,
        max_length=128,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password')
        read_only_fields = ('username',)


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=7,
        max_length=30,
        write_only=True
    )
    password = serializers.CharField(
        min_length=4,
        max_length=128,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ChangeUserPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
