from django.conf import settings
from django.core.mail import send_mail

from chatbot.models import Notification


class NotificationProcessor:

    def __init__(self, notification: Notification):
        self.notification = notification

        self.notification_map = {
            'welcome': {
                'subject': self.get_welcome_subject,
                'message': self.get_welcome_message,
            }
        }

    def get_welcome_subject(self) -> str:
        """Returns the subject for the welcome email"""

        return 'Welcome {}'.format(self.notification.user.username)

    def get_welcome_message(self) -> str:
        """Returns the message for the welcome email"""

        return 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
                Lorem Ipsum has been the industry standard dummy text ever since the 1500s.'

    def send(self) -> None:
        """Send the notification email"""

        _type = self.notification.extra_data['type']

        send_mail(
            self.notification_map[_type]['subject'](),
            self.notification_map[_type]['message'](),
            settings.EMAIL_FROM,
            [self.notification.user.email],
            fail_silently=False,
        )

        self.notification.sent = True
        self.notification.save()
