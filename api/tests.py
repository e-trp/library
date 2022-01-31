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
        
        dt_now = datetime.datetime.now().isoformat()
        for i in range(2):
            Book.objects.create(
                name = 'book' + str(i),
                author = test_author,
                language = 'ru',
                publish_date = dt_now 
            )
            
    def test_get_book_list(self):
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token)
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_authors_list(self):
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token)
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscriber_list(self):
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token)
        response = self.client.get('/api/subscribers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



# class RetriveObjectsTest(APITestCase):

#     def setUp(self):
#         test_author = Author.objects.create(
#             first_name = "tes author", 
#             mid_name = "tes author",
#             last_name ="tes author"
#         )
#         dt_now = datetime.datetime.now().isoformat()
#         for i in range(2):
#             Book.objects.create(
#                 name = 'book' + str(i),
#                 author = test_author,
#                 language = 'ru',
#                 publish_date = dt_now 
#             )
#         request_data = {
#             "username": "test_user1",
#             "password": "S@3cr33t",
#         }
#         response = self.client.post(
#             '/api/auth/', 
#             request_data, format="json"
#         )
#         self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + response.data["token"])

#     def test_book_list(self):
#         response = self.client.get('/api/books/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
