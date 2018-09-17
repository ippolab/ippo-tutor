from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIRequestFactory

from ..models import User


class UsersRequestsTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        self.student_user = User.objects.create_user(username='studentuser', password='studentpassword')
        self.tutor_user = User.objects.create_user(username='tutoruser', password='tutorpassword', is_tutor=True)