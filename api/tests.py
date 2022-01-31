from unicodedata import name
from urllib import request
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book, Subscriber, Author
import datetime
import json

# Create your tests here.

class AppTest(APITestCase):

    def setUp(self):
        self.user_data = {
          "username": "test_user1",
          "password": "S3cr33t111",
          "email": "test_user1@example.com"
        }
        response = self.client.post(
            '/api/register/',
            self.user_data, 
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(
            '/api/auth/',
             self.user_data, 
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.token = response.data['token']

        test_author = Author.objects.create(
            first_name = "tes author", 
            mid_name = "tes author",
            last_name ="tes author"
        )
        
        dt_now = datetime.datetime.now()
        dt_str = dt_now.isoformat()
        test_book = Book.objects.create(
                name = 'test_book',
                author = test_author,
                language = 'ru',
                publish_date = dt_str 
            )
        new_date = dt_now + datetime.timedelta(days=400) 
        new_book = Book.objects.create(
            name = 'new_book', 
            author = test_author,
            language = 'ru',
            publish_date = new_date
        )
        self.new_book_id = new_book.id
        self.test_book_id = test_book.id

    def test_get_book_list(self):
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token)
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book(self):
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token)
        response = self.client.get('/api/books/{0}/'.format(self.test_book_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forbidden_new_book(self):
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token)
        response = self.client.get('/api/books/{0}/'.format(self.new_book_id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_authors_list(self):
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token)
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscriber_list(self):
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token)
        response = self.client.get('/api/subscribers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

