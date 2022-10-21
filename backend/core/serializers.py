from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'bio', 'country', 'date_of_birth')
        write_only_fields = ('username', 'password')


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=40, allow_blank=False)
    email = serializers.EmailField(max_length=80, allow_blank=False)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

    def validate(self, attrs):
        existing = User.objects.filter(username=attrs.get('username')).first()
        if existing:
            raise serializers.ValidationError("Someone with that username address has already registered.")
        return super(UserCreationSerializer, self).validate(attrs)

    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.password = make_password(validated_data.get('password'))
        new_user.save()
        return new_user
