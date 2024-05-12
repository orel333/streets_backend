from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    '''Модель для постов в блоге'''
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=200
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
