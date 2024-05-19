from rest_framework import serializers
from blog.models import BlogPost

from utils.fields import Base64ImageField


class BlogPostSerializer(serializers.ModelSerializer):
    '''Сериализатор для постов в блоге'''
    image = Base64ImageField(required=True, allow_null=False)
    author = serializers.SlugRelatedField(
        slug_field='username'
    )
    region = serializers.SlugRelatedField(
        many=True,
        slug_field='name'
    )

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at',
            'image',
            'type',
            'relevance_date',
            'region'
        ]

    #TODO валидация type, создание relevance_date
