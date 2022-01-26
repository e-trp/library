from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.serializers import BookSerializer, AuthorSerializer, SubscriberSerializer
from api.models import Author, Book, Subscriber



class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SubscriberViewSet(ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
