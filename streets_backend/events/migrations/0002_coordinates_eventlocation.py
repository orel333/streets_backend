# Generated by Django 4.2.7 on 2024-05-22 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название места')),
                ('description', models.TextField(verbose_name='Описание места')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.coordinates', verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Место проведения мероприятия',
                'verbose_name_plural': 'Места проведения мероприятий',
            },
        ),
    ]
