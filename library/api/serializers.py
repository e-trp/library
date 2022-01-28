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


class UserAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

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


class AuthTokenSerializer(Serializer):
    username = CharField(label="Username")
    password = CharField(label="Password", style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')
        if username and password:
            user = authenticate(email=username, password=password)
            if user:
                if user.is_deleted:
                    raise ValidationError('User account is deleted.', code='authorization')
            else:
                raise ValidationError('Unable to log in with provided credentials.', code='authorization')
        else:
            raise ValidationError('Must include "email" and "password".', code='authorization')

        attrs['user'] = user
        return attrs