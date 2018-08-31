import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models

from ippo_tutor.apps.students.models import StudentProfile
from ippo_tutor.apps.tutors.models import TutorProfile


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, **kwargs):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Subject(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class SubjectType(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


def upload(instance: 'Work', file_name):
    file_path = os.path.join("students_files",
                             instance.student.group.__str__(),
                             instance.student.__str__(),
                             instance.subject.__str__(),
                             instance.subject_type.__str__(),
                             file_name)
    return file_path


class Work(models.Model):
    STATUSES = (
        ('accepted', 'accepted'),
        ('to fix', 'to fix'),
        ('not done', 'not done'),
    )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=8, choices=STATUSES, default='not done')

    file = models.FileField(storage=OverwriteStorage(), upload_to=upload, null=True)

    loaded = models.DateTimeField(auto_now_add=True)
    checked = models.DateTimeField(null=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='works')
    tutor = models.ForeignKey(TutorProfile, null=True, on_delete=models.SET_NULL, related_name='works')
