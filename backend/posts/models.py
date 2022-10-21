from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    body = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='likes', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.PROTECT)
