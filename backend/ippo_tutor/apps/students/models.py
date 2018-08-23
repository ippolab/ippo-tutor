from django.db import models

from ippo_tutor.apps.authentication.models import UserProfile


class StudentProfile(UserProfile):
    first_name = models.CharField(max_length=255, blank=True)
    second_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.second_name, self.last_name)
