from django.urls import path

from chatbot.api.v1.views import ListCreateUsersAPIView

urlpatterns = [
    path(
        'users/',
        ListCreateUsersAPIView.as_view(),
        name='list-create-users',
    ),
]
