from django.forms import models
from rest_framework.serializers import ModelSerializer, Serializer
from api.models import Author, Book, Subscriber


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class SubscriberSerializer(ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'