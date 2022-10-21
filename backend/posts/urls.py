from django.contrib import admin
from django.urls import path
from .views import PostList, PostUpdateDelete, PostLike, PostUnLike

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostUpdateDelete.as_view()),
    path('posts/<int:pk>/like', PostLike.as_view()),
    path('posts/<int:pk>/unlike', PostUnLike.as_view()),

]