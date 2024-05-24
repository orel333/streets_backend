from rest_framework import viewsets

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer
from utils.permissions import OwnerOrReadOnly


class BlogPostViewSet(viewsets.ModelViewSet):
    '''ViewSet для модели BlogPost'''
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
