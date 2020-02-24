from rest_framework import serializers
from app.models import *
from rest_framework_recursive.fields import RecursiveField

class TagSerializer(serializers.ModelSerializer):
    """Поля тегов"""

    class Meta:
        model=Tag
        fields = (
            'name',
            'published'
        )


"""class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer=self.parent.parent.__class__(value, context=self.context)
        return serializer.data"""

class CatSerializer(serializers.ModelSerializer):
    """Поля категорий"""
    #parentCat = serializers.CharField(Cat.get_par_cat)
    #subcat=serializers.SubCatSerializer()
    class Meta:
        model = Cat
        fields = (
            'id',
            'name',
            'description',
            'published',
            #'parentCat'
        )

class PostSerializer(serializers.ModelSerializer):
    """поля постов"""
    category=CatSerializer(many=False, read_only=True)
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
            'status',
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

