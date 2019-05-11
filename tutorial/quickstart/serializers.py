from django.contrib.auth.models import User, Group, Post, Catagory, ContentType
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'username')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'tags', 'publish_time', 'author_id', 'category_name', 'content_type')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'content', 'publish_time', 'author_name', 'author_email', 'post_id')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name', 'description')

class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ContentType
    fields = ('id', 'type_name')