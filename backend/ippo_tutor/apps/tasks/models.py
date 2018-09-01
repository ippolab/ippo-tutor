from django.db import models
from django.core.validators import FileExtensionValidator

import os

from ippo_tutor.apps.works.models import Subject, SubjectType, Work, OverwriteStorage
from ippo_tutor.apps.students.models import Group
from ippo_tutor.apps.tutors.models import TutorProfile


def upload(instance, file_name):
    file_path = os.path.join(
        'tasks_files',
        str(instance.group),
        str(instance.subject),
        str(instance.subject_type),
        file_name
    )

    return file_path


class Task(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    description = models.CharField(max_length=511, blank=False, null=False)
    zip_with_templates = models.FileField(
        upload_to=upload,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=['zip'])],
        null=True
    )
    changed = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(TutorProfile, null=True, on_delete=models.SET_NULL)
