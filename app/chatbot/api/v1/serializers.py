from rest_framework import serializers

from chatbot.models import CustomUser, Notification


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone']

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)

        Notification.objects.create(
            user=user,
            via=Notification.EMAIL,
            extra_data={'type': 'welcome'},
        )

        return user
