from rest_framework import generics, permissions
from rest_framework.views import APIView
from api.somesite.serializers import *
from app.models import *
from django.http.response import *

#class PostShortList(APIView):
#    permission_classes = [permissions.AllowAny],
#    def get(self,request, format=None):
#        post=Post.objects.all()
#        serializer=PostShortSerializer(post, many=False)
#        return (data=serializer.data)

class PostShortList(generics.ListAPIView):
    """Короткая инфа по посту для персика"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostShortSerializer

class CatList(generics.ListAPIView):
    """Список категорий"""
    permission_classes = [permissions.AllowAny]
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class TagList(generics.ListAPIView):
    """Список тегов"""
    permission_classes = [permissions.AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostList(generics.ListAPIView):
    """Список постов"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListAPIView):
    """Список комментов"""
    permission_classes = [permissions.AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CreatePost(generics.CreateAPIView):
    """Создание поста"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
