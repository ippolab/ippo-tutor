from django.core.validators import FileExtensionValidator
from django.db import models

from ippo_tutor.apps.students.models import StudentProfile
from ippo_tutor.apps.tutors.models import TutorProfile
from ippo_tutor.apps.tasks.models import Task
from ippo_tutor.apps.core import storage


class Work(models.Model):
    class Meta:
        unique_together = (('task', 'student'),)

    STATUSES = (
        ('A', 'Accepted'),
        ('F', 'To fix'),
        ('N', 'Not done'),
    )
    status = models.CharField(max_length=1, choices=STATUSES, default='N', blank=False)
    document = models.FileField(
        upload_to=storage.upload_work,
        storage=storage.OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        null=True
    )
    source_code = models.FileField(
        upload_to=storage.upload_work,
        storage=storage.OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=['zip'])],
        null=True
    )
    checked = models.DateTimeField(null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='works')
    tutor = models.ForeignKey(TutorProfile, null=True, on_delete=models.SET_NULL, related_name='works')

    def __str__(self):
        return self.task.title
