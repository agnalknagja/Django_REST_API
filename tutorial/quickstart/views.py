from django.contrib.auth.models import User
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer, ContentTypeSerializer

class User(models.Model):
    
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  username = models.CharField(max_length=50)

class Post(models.Model):
  
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=100)
  tags = models.CharField(max_length=25)
  publish_time = models.Datefield()
  author_id = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

 








class Category(models.Model):
  name = models.CharField(max_length=25)
  description = models.CharField(max_length=100)

class ContentType(models.Model):
  type_name = models.CharField(max_length=25)


