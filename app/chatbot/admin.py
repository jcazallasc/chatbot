from django.contrib import admin

from chatbot.models import CustomUser, Notification

admin.site.register(CustomUser)
admin.site.register(Notification)
