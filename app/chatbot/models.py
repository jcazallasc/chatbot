from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField()
    phone = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.username


class Notification(models.Model):

    EMAIL = 'Email'
    VIA_CHOICES = [
        (EMAIL, _('Email')),
    ]

    user = models.ForeignKey(
        CustomUser,
        related_name='notifications',
        on_delete=models.CASCADE,
    )
    via = models.CharField(
        max_length=140,
        choices=VIA_CHOICES,
        default=EMAIL,
    )
    extra_data = JSONField(blank=True, null=True)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return 'Notification to {} via {}'.format(self.user.username, self.via)
