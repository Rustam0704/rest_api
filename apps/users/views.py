from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User, Post, Comment
from apps.users.serializers import UserSerializer, UserCreateSerializer, PostSerializer, PostCreateSerializer, \
    CommentSerializer


class UserAPIView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(data={'detail': 'User created'}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        # serializer = UserSerializer(user)
        return Response(data={"detail": 'User deleted'}, status=status.HTTP_204_NO_CONTENT)

class PostAPIView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer =PostSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer =PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return Response(data={'detail': 'Post created'}, status=status.HTTP_201_CREATED)


class CommentAPIView(APIView):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer =CommentSerializer(comment)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

