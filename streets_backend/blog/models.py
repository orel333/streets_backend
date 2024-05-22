from django.db import models
from users.models import CustomUser


class BlogPost(models.Model):
    '''Модель для постов в блоге'''
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Автор поста'
    )
    title = models.CharField(
        'Заголовок',
        max_length=200
    )
    content = models.TextField(
        'Содержание'
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Пост блога'
        verbose_name_plural = 'Посты блога'
