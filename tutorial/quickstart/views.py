from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer, ContentTypeSerializer