from django.db import models


class Event(models.Model):
    """Модель мероприятия для интерактивного календаря"""
    name = models.CharField(
        'Название мероприятия',
        max_length=255
    )
    time = models.TimeField(
        'Время проведения'
    )
    date = models.DateField(
        'Дата проведения'
    )
    place = models.CharField(
        'Место проведения',
        max_length=255
    )
    description = models.TextField(
        'Описание мероприятия'
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name
