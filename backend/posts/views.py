from django.db.models import Count, Sum
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly

from .serializers import PostSerializer
from .models import Post, Like


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Post.objects.annotate(
            total_likes=Count('likes__body')
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostLike(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        like = Like.objects.filter(owner=request.user, post=kwargs.get('pk')).first()
        if like:
            if not like.body:
                like.body = True
                like.save()
        else:
            Like.objects.create(
                body=True,
                owner=request.user,
                post=Post.objects.filter(id=kwargs.get('pk')).first()
            )
        return Response({'result': 'success'})


class PostUnLike(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        like = Like.objects.filter(owner=request.user, post=kwargs.get('pk')).first()
        if like:
            like.delete()
            return Response({'result': 'remove like success'})
        else:
            return Response({'result': 'like doesn\'t exist'})
