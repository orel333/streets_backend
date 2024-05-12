from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    '''Вьюсет для постов в блоге'''
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
