from rest_framework import serializers
from app.models import *

class TagSerializer(serializers.ModelSerializer):
    """Поля тегов"""

    class Meta:
        model=Tag
        fields = (
            'name',
            'published'
        )

class CatSerializer(serializers.ModelSerializer):
    """Поля категорий"""
    #parent = serializers.Field(source='parent')  # завязка модели саму на себя
    class Meta:
        model = Cat
        fields = (
            'name',
            'description',
            'published',
            'parent'
        )

class PostSerializer(serializers.ModelSerializer):
    """поля постов"""
    #category=CatSerializer(many=True)
    tags=TagSerializer(many=True)
    class Meta:
        model=Post
        fields=(
            'author',
            'title',
            'text',
            'subtitle',
            'created_date',
            'image',
            'edit_date',
            'published_date',
            'tags',
            'category',
            'published',
            'viewed',
            'status'
        )

class CommentSerializer(serializers.ModelSerializer):
    """Поля комментов"""
    #post=PostSerializer(many=True)
    class Meta:
        model=Comment
        fields = (
            'author',
            'text',
            'created_date',
            'moderation',
            'post'
        )

