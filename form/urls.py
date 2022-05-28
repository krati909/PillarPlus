from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from form.views import UserViewSet

router= routers.DefaultRouter
router.register('User',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]