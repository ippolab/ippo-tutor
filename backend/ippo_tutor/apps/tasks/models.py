from django.db import models
from django.core.validators import FileExtensionValidator

from ippo_tutor.apps.tutors.models import TutorProfile
from ippo_tutor.apps.students.models import Group
from ippo_tutor.apps.core import storage


class Subject(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class SubjectType(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        unique_together = (('title', 'group', 'subject', 'subject_type',),)

    zip_with_templates = models.FileField(
        upload_to=storage.upload_task,
        storage=storage.OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=['zip'])],
        null=True
    )
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=False, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    tutor = models.ForeignKey(TutorProfile, null=True, on_delete=models.SET_NULL)
