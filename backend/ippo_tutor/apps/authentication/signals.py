from django.db.models.signals import post_save
from django.dispatch import receiver

from ippo_tutor.apps.students.models import StudentProfile
from ippo_tutor.apps.tutors.models import TutorProfile

from .models import User


@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    if instance and created:
        if instance.is_tutor:
            instance.tutor = TutorProfile.objects.create(user=instance)
        else:
            instance.student = StudentProfile.objects.create(user=instance)
        instance.save()
