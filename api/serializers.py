import email
from rest_framework.serializers import ModelSerializer, Serializer, CharField, ValidationError, EmailField
from api.models import Author, Book, Subscriber
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


User = get_user_model()


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


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'email': {
                'required': True,
                'allow_blank': False
            }
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def to_representation(self, instance):
        data = {
            'username': instance.username,
            'email': instance.email
        }
        return data
