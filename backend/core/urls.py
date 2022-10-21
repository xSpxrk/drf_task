from django.contrib import admin
from django.urls import path
from .views import UserCreate, UserAPIUpdateDelete, UserAPIList

urlpatterns = [
    path('users/', UserAPIList.as_view()),
    path('users/signup/', UserCreate.as_view()),
    path('users/<int:pk>/', UserAPIUpdateDelete.as_view()),
]