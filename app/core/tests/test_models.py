from django.test import TestCase
from django.contrib.auth import get_user_model


def sample_user(email="test@gmail.com", password='testpass'):
    """Creates a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_user_create_with_email(self):
        """Test that new user with email is successfull"""
        email = 'test@gmail.com'
        password = 'Testpassdgf'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that email for new user is normalized"""
        email = 'test@GMAIL.COM'

        user = get_user_model().objects.create_user(email, 'tes123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that creating user with invalid email rasise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test34')
