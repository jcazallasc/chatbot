from rest_framework import generics

from chatbot.api.v1.pagination import SmallSetPagination
from chatbot.api.v1.serializers import CustomUserSerializer
from chatbot.models import CustomUser


class ListCreateUsersAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer
    pagination_class = SmallSetPagination
