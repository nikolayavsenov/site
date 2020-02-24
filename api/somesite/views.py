from rest_framework import generics, permissions
from api.somesite.serializers import *
from app.models import *


class CatList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class TagList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
