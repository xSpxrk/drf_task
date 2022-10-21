from rest_framework import serializers
from rest_framework.relations import ManyRelatedField

from .models import Post, Like
from django.contrib.auth.hashers import make_password
from core.serializers import UserSerializer
from django.db.models import Count, Case, When


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('body',)


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(serializers.ReadOnlyField(source='owner'), read_only=True)
    total_likes = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'total_likes']
