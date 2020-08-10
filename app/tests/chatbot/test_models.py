from django.db.utils import IntegrityError
from django.test import TestCase

from chatbot.models import Notification
from tests.utils import sample_notification, sample_user


class UserTest(TestCase):

    def test_create_user_successful(self):
        """Test creating a new user successful"""

        username = 'test'
        email = 'test@test.com'
        phone = '123123123'

        user = sample_user(username=username, email=email, phone=phone)

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertEqual(user.phone, phone)

    def test_create_user_with_no_email(self):
        """Test creating a new user with no email"""

        username = 'test'
        email = None
        phone = '123123123'

        with self.assertRaises(IntegrityError):
            sample_user(username=username, email=email, phone=phone)

    def test_create_user_with_no_phone(self):
        """Test creating a new user with no email"""

        username = 'test'
        email = 'test@test.com'
        phone = None

        with self.assertRaises(IntegrityError):
            sample_user(username=username, email=email, phone=phone)

    def test_create_user_duplicating_username(self):
        """Test creating a new user duplicating username"""
        sample_user()

        with self.assertRaises(IntegrityError):
            sample_user()


class NotificationTest(TestCase):

    def test_create_notification_successful(self):
        """Test creating notification successful"""

        user = sample_user()

        notification = sample_notification(user=user)

        self.assertEqual(notification.user, user)
        self.assertEqual(notification.via, Notification.EMAIL)
        self.assertEqual(notification.extra_data, {})
        self.assertEqual(notification.sent, False)
