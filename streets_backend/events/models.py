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


class Coordinates(models.Model):
    """Модель для хранения координат места проведения мероприятия"""
    latitude = models.DecimalField(
        'Широта',
        max_digits=9,
        decimal_places=6
    )
    longitude = models.DecimalField(
        'Долгота',max_digits=9,
        decimal_places=6
    )

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"


class EventLocation(models.Model):
    """Модель места проведения мероприятия"""
    name = models.CharField(
        'Название места',
        max_length=255
    )
    description = models.TextField(
        'Описание места'
    )
    address = models.CharField(
        'Адрес',
        max_length=255
    )
    coordinates = models.ForeignKey(
        Coordinates,
        on_delete=models.CASCADE,
        verbose_name='Координаты'
    )

    class Meta:
        verbose_name = 'Место проведения мероприятия'
        verbose_name_plural = 'Места проведения мероприятий'

    def __str__(self):
        return self.name
