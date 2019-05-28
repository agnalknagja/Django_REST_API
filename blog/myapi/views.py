from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse


from myapi.models import User, Post, Comment, Category, ContentType
from myapi.serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer, ContentTypeSerializer

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'user': reverse('user', request=request, format=format),
    'post': reverse('post', request=request, format=format),
    'comment': reverse('comment', request=request, format=format),
    'category': reverse('category', request=request, format=format),
    'contenttype': reverse('contenttype', request=request, format=format),
  })


  

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post .objects.all()
  serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class ContentTypeViewSet(viewsets.ModelViewSet):
  queryset = ContentType.objects.all()
  serializer_class = ContentTypeSerializer
