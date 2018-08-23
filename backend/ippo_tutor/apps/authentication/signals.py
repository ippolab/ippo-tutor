from django.db.models.signals import post_save
from django.dispatch import receiver

from ippo_tutor.apps.students.models import StudentProfile

from .models import User


@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    if instance and created:
        if instance.is_tutor:
            raise NotImplementedError('Not supported now')
        else:
            instance.profile = StudentProfile.objects.create(user=instance)
            instance.save()
