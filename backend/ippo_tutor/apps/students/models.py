from django.db import models

from ippo_tutor.apps.authentication.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')

    first_name = models.CharField(max_length=255, blank=True)
    second_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.second_name, self.last_name)


class Group(models.Model):
    name = models.CharField(max_length=255, blank=True)
