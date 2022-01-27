from rest_framework.viewsets import ModelViewSet
from api.serializers import BookSerializer, AuthorSerializer, SubscriberSerializer
from api.models import Author, Book, Subscriber
from rest_framework.permissions import IsAdminUser
from api.permissions import LibraryPermission
from api.tasks import send_mail_to_subs



class AuthorViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        print('reform create')
        send_mail_to_subs.delay(None)



class SubscriberViewSet(ModelViewSet):
    permission_classes = [LibraryPermission | IsAdminUser]
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
