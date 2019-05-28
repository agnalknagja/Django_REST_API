from django.db import models


class User(models.Model):  
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  username = models.CharField(max_length=50)

class Category(models.Model):
  name = models.CharField(max_length=25)
  description = models.CharField(max_length=100)

class ContentType(models.Model):
  type_name = models.CharField(max_length=25)

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=100)
  tags = models.CharField(max_length=25)
  publish_time = models.DateField(default=None, null=True)
  author_id = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
  category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
  content = models.CharField(max_length=1000)
  publish_time = models.DateField(default=None, null=True)
  author_name = models.CharField(max_length=50)
  author_email = models.CharField(max_length=100)
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

