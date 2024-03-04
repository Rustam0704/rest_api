from datetime import timezone

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.users.models import User, Post
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'username', 'first_name', 'last_name')


class UserCreateSerializer(ModelSerializer):
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone', 'username', 'first_name', 'last_name', "password1", "password2")

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise ValidationError('passwords did not match')

        return attrs

    def validate_username(self, value):
        if not value.isalpha():
            raise ValidationError("username must contains only letters")
        return value

    def create(self, validated_data):
        password = validated_data['password1']
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        phone = validated_data['phone']
        user = User.objects.create(username=username, phone=phone, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'user', 'is_active')

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields = ('id', 'title', 'body', 'user', 'is_active')

    def create(self, validated_data):
        title = validated_data['title']
        body = validated_data['body']
        user = validated_data['user']
        is_active = validated_data['is_active']
        post = Post(title=title, body=body, user=user, is_active=is_active)
        post.save()
        return post

