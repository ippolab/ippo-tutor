from django.db import models

from ippo_tutor.apps.students.models import StudentProfile
from ippo_tutor.apps.tutors.models import TutorProfile


class Subject(models.Model):
    name = models.CharField(max_length=16)


class SubjectType(models.Model):
    name = models.CharField(max_length=12)


class Work(models.Model):
    STATUSES = (
        ('accepted', 'accepted'),
        ('to fix', 'to fix'),
        ('not done', 'not done'),
    )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=8, choices=STATUSES, default='not done')

    file = models.FileField(null=True)

    loaded = models.DateTimeField(auto_now_add=True)
    checked = models.DateTimeField(null=True)

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='works')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    tutor = models.ForeignKey(TutorProfile, null=True, on_delete=models.SET_NULL, related_name='works')
