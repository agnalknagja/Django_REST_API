from django.shortcuts import render
from myapi.models import User, Post, Comment, Category, ContentType
from myapi.serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer, ContentTypeSerializer

class UserViewSet(viewsets.ModelViewSet):

class PostViewSet(viewsets.ModelViewSet):

class CommentViewSet(viewsets.ModelViewSet):

class CategoryViewSet(viewsets.ModelViewSet):

class ContentTypeViewSet(viewsets.ModelViewSet):

