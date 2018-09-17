from django.test import TestCase

from ippo_tutor.apps.tutors.models import TutorProfile
from ippo_tutor.apps.students.models import StudentProfile

from ..models import User


class SignalTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.student = User.objects.create_user(username='studentuser')
        cls.tutor = User.objects.create_user(username='tutoruser', is_tutor=True)
        cls.admin = User.objects.create_superuser(username='admin', password='adminpassword')

    def test_create_related_profile(self):
        with self.assertRaises(TutorProfile.DoesNotExist):
            _ = self.student.tutor
        with self.assertRaises(StudentProfile.DoesNotExist):
            _ = self.tutor.student
        with self.assertRaises(StudentProfile.DoesNotExist):
            _ = self.admin.student

        _ = self.student.student
        _ = self.tutor.tutor
        _ = self.admin.tutor
