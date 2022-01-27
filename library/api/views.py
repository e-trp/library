from rest_framework.viewsets import ModelViewSet
from api.serializers import BookSerializer, AuthorSerializer, SubscriberSerializer
from api.models import Author, Book, Subscriber
from rest_framework.permissions import IsAdminUser
from api.permissions import LibraryPermission



class AuthorViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SubscriberViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
