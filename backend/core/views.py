from rest_framework import generics, permissions

from rest_framework.response import Response

from .models import User

from .serializers import UserSerializer, UserCreationSerializer
from .permissions import IsOwnerOrReadOnly


class UserAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = UserCreationSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserAPIUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
