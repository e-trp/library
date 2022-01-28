from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import BookSerializer, AuthorSerializer, SubscriberSerializer, UserRegisterSerializer
from api.models import Author, Book, Subscriber
from api.permissions import LibraryUserPermission, AdminPermission, BooksPermission
from api.tasks import send_mail_to_subs
from django.contrib.auth import get_user_model


User = get_user_model()


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


class UserRegistration(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
