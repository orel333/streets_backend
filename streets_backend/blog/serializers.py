from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    '''Сериализатор для постов в блоге'''
    class Meta:
        model = BlogPost
        fields = [
            'id', 'author', 'title', 'content', 'created_at', 'updated_at'
        ]
