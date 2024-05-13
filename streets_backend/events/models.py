from django.db import models


class Event(models.Model):
    """Модель мероприятия для интерактивного календаря"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название мероприятия'
    )
    time = models.TimeField(
        verbose_name='Время проведения'
    )
    date = models.DateField(
        verbose_name='Дата проведения'
    )
    place = models.CharField(
        max_length=255,
        verbose_name='Место проведения'
    )
    description = models.TextField(
        verbose_name='Описание мероприятия'
    )

    def __str__(self):
        return self.name
