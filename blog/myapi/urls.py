from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from myapi import views

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)
router.register('category', views.CategoryViewSet)
router.register('contenttype', views.ContentTypeViewSet)

urlpatterns = [
  path('', include(router.urls))
]
