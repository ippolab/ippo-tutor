from django.test import TestCase

from ..models import User, UserManager


class UserManagerModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.manager = UserManager()

    def test_create_superuser_without_password(self):
        with self.assertRaises(ValueError, msg='Password for superusers must be set'):
            self.manager.create_superuser(username='admin')


class UserModelTest(TestCase):
    def setUp(self):
        self.simpleuser = User.objects.create_user(username='simpleuser')
        self.simpletutor = User.objects.create_user(username='simpletutor', is_tutor=True)
        self.adminuser = User.objects.create_superuser(username='adminuser', password='adminpassword')

    def test_simple_user_creation(self):
        self.assertFalse(self.simpleuser.is_tutor)

    def test_tutor_user_creation(self):
        self.assertTrue(self.simpletutor.is_tutor)

    def test_admin_user_creation(self):
        self.assertTrue(self.adminuser.is_tutor)
        self.assertTrue(self.adminuser.is_staff)

    def test_user_str(self):
        self.assertEqual(str(self.simpleuser), 'simpleuser')
