from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from quickstart import views


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]