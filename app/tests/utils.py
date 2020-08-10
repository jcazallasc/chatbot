from chatbot.models import CustomUser, Notification


def sample_user(username='testing', email='testing@testing.com', phone='999999999'):
    return CustomUser.objects.create(
        username=username,
        email=email,
        phone=phone,
    )

def sample_notification(user, via=Notification.EMAIL, extra_data={}, sent=False):
    return Notification.objects.create(
        user=user,
        via=via,
        extra_data=extra_data,
        sent=sent,
    )
