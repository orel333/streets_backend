from rest_framework import viewsets
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    '''ViewSet для модели BlogPost'''
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
