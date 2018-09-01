import os

from django.core.validators import FileExtensionValidator
from django.core.files.storage import FileSystemStorage
from django.conf import settings
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


def upload(instance, file_name):
    file_path = os.path.join(
        'students_files',
        str(instance.student.group),
        str(instance.student),
        str(instance.subject),
        str(instance.subject_type),
        str(instance.title),
        file_name
    )

    return file_path


class Work(models.Model):
    STATUSES = (
        ('A', 'Accepted'),
        ('F', 'To fix'),
        ('N', 'Not done'),
    )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUSES, default='N')

    file = models.FileField(
        upload_to=upload,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'zip'])],
        null=True
    )

    loaded = models.DateTimeField(auto_now_add=True)
    checked = models.DateTimeField(null=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='works')
    tutor = models.ForeignKey(TutorProfile, null=True, on_delete=models.SET_NULL, related_name='works')

    def __str__(self):
        return self.title
