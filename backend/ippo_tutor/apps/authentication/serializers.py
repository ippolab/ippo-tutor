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
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ChangeUserPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
