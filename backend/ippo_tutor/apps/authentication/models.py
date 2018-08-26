from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager


class UserManager(DefaultUserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        if not password:
            raise ValueError('Password for superusers must be set')

        extra_fields.setdefault('is_tutor', True)
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
