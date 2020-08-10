import time

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

from chatbot.models import Notification
from chatbot.notifications.notification_processor import NotificationProcessor


class Command(BaseCommand):
    """Django command to read pending notifications"""

    def handle(self, *args, **options):
        """Handle the command"""

        notifications = Notification.objects.filter(sent=False).filter(
            via=Notification.EMAIL).order_by('id')[:settings.DIGEST_NOTIFICATION_BATCH]

        for notification in notifications:
            NotificationProcessor(notification=notification).send()
