from django.db import models


class Contact(models.Model):
    """Модель контактов"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название организации'
    )
    inn = models.CharField(
        max_length=12,
        verbose_name='ИНН'
    )
    ogrn = models.CharField(
        max_length=13,
        verbose_name='ОГРН'
    )
    legal_address = models.CharField(
        max_length=255,
        verbose_name='Юридический адрес'
    )
    actual_address = models.CharField(
        max_length=255,
        verbose_name='Фактический адрес'
    )
    email = models.EmailField()
    phone = models.CharField(max_length=20)
