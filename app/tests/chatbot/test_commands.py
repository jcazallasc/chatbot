import csv
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase

from chatbot.models import CustomUser, Notification
from tests.utils import sample_notification, sample_user


class CommandsTestCase(TestCase):

    @patch('chatbot.notifications.notification_processor.send_mail')
    def test_digest_notifications(self, mock_send_mail):
        """Test digest notifications"""

        user = sample_user()
        notification = sample_notification(user=user, extra_data={'type': 'welcome'})

        call_command('digest_notifications')

        self.assertTrue(mock_send_mail.called)

        notification = Notification.objects.get(id=notification.id)

        self.assertTrue(notification.sent)
