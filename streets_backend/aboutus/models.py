from django.db import models


class AboutUs(models.Model):
    """Модель для информации о нас"""
    mission = models.TextField(
        verbose_name='Миссия'
    )
    history = models.TextField(
        verbose_name='История'
    )

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class FederalTeam(models.Model):
    """Модель для федеральной команды"""
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Федеральная команда'
        verbose_name_plural = 'Федеральные команды'


class RegionalTeam(models.Model):
    """Модель для региональной команды"""
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    region = models.CharField(
        max_length=255,
        verbose_name='Регион'
    )

    class Meta:
        verbose_name = 'Региональная команда'
        verbose_name_plural = 'Региональные команды'


class PartnerType(models.Model):
    """Модель для типов партнеров"""
    TYPE_CHOICES = [
        ('general', 'Генеральные партнеры'),
        ('strategic', 'Стратегические партнеры'),
        ('organizational', 'Организационные партнеры'),
        ('regional', 'Региональные партнеры'),
    ]

    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        verbose_name='Тип'
    )

    class Meta:
        verbose_name = 'Тип партнера'
        verbose_name_plural = 'Типы партнеров'


class Partner(models.Model):
    """Модель для партнеров"""
    name = models.CharField(
        max_length=255, 
        verbose_name='Имя'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    type = models.ForeignKey(
        PartnerType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тип'
    )

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Gallery(models.Model):
    """Модель для галереи"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Media(models.Model):
    """Модель для медиа (видео или фото)"""
    gallery = models.ForeignKey(
        Gallery, 
        on_delete=models.CASCADE
    )
    file = models.FileField(
        upload_to='media/'
    )

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'
