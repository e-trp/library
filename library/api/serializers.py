from django.forms import models
from rest_framework.serializers import ModelSerializer, Serializer
from api.models import Author, Book, Subsciber


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book


class SubscriberSerializer(ModelSerializer):
    class Meta:
        model = Subsciber