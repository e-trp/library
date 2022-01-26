from distutils.command.config import LANG_EXT
from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    mid_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)


class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(Author, null=True, blank=False, on_delete=models.SET_NULL)
    language = models.CharField(max_length=50, null=False, blank=False)
    publish_date = models.DateTimeField(null=False, blank=False)

    
class Subscriber(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    mid_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)