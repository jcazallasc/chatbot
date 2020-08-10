import json
from datetime import date
from unittest.mock import MagicMock, patch

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from chatbot.models import CustomUser, Notification

USERS_URL = 'list-create-users'


class ChatBotV1ApiTests(TestCase):
    """Test for the API V1 of chatbot"""

    def setUp(self):
        self.client = APIClient()

    def test_user_list(self):
        """Test listing users with a valid request"""

        res = self.client.get(reverse(USERS_URL))

        users_count = CustomUser.objects.all().count()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['count'], users_count)

    def test_create_user_successfully(self):
        """Test create user successfully"""

        username = 'test'
        email = 'test@test.com'
        phone = '123456789'

        res = self.client.post(
            reverse(USERS_URL),
            {
                'username': username,
                'email': email,
                'phone': phone,
            },
        )

        user = CustomUser.objects.get(username=username)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(user.notifications.count(), 1)

    def test_create_user_with_no_email(self):
        """Test create user without email"""

        username = 'test'
        phone = '123456789'

        res = self.client.post(
            reverse(USERS_URL),
            {
                'username': username,
                'phone': phone,
            },
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_no_phone(self):
        """Test create user without email"""

        username = 'test'
        email = 'test@test.com'

        res = self.client.post(
            reverse(USERS_URL),
            {
                'username': username,
                'email': email,
            },
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
