from django.contrib.auth.models import User
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer, ContentTypeSerializer

class User(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)




