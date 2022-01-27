from rest_framework.viewsets import ModelViewSet
from api.serializers import BookSerializer, AuthorSerializer, SubscriberSerializer
from api.models import Author, Book, Subscriber
from api.permissions import LibraryUserPermission, AdminPermission, BooksPermission
from api.tasks import send_mail_to_subs
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class AuthorViewSet(ModelViewSet):
    permission_classes = [AdminPermission | LibraryUserPermission]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [AdminPermission | BooksPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'language', 'publish_date']
    search_fields = ['name', 'language', 'publish_date']
    order_fields = ['publish_date']

    def perform_create(self, serializer):
        super().perform_create(serializer)
        send_mail_to_subs.delay(serializer.instance.id)


class SubscriberViewSet(ModelViewSet):
    permission_classes = [AdminPermission | LibraryUserPermission]
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
