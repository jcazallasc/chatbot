from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    """Custom small pagination"""

    page_size = 10
