from rest_framework.viewsets import ModelViewSet
from api.serializers import BookSerializer, AuthorSerializer, SubscriberSerializer
from api.models import Author, Book, Subscriber
from rest_framework.permissions import IsAdminUser
from api.permissions import LibraryPermission
from api.tasks import send_mail_to_subs
from django_filters.rest_framework import DjangoFilterBackend



class AuthorViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'language', 'publish_date']

    def perform_create(self, serializer):
        super().perform_create(serializer)
        send_mail_to_subs.delay(serializer.instance.id)


class SubscriberViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
