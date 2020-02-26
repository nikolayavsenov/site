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


class PostShortSerializer(serializers.ModelSerializer):
    category = CatSerializer(many=False, read_only=True)
    class Meta:
        model=Post
        fields = (
            'title',
            'category',
            'text',
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


class PostidSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id',)


class CreatePostSerializer(serializers.ModelSerializer):
    """Создание поста"""
    category=Cat.objects.name
    #id=Post.objects.get('id')
    class Meta:
        model=Post
        fields=(
            #'id',
            'author',
            'title',
            'text',
            'slug',
            'subtitle',
            'category',
            'created_date',
            'image',
            'edit_date',
            'published_date',
            'published',
            'viewed',
            'status',
        )
    def create(self, request):
        creation = Post.objects.create(**request)
        return  creation