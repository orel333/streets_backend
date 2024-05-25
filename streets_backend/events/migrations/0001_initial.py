from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название мероприятия')),
                ('time', models.TimeField(verbose_name='Время проведения')),
                ('date', models.DateField(verbose_name='Дата проведения')),
                ('place', models.CharField(max_length=255, verbose_name='Место проведения')),
                ('description', models.TextField(verbose_name='Описание мероприятия')),
                ('region', models.CharField(max_length=255, verbose_name='Регион')),
                ('event_type', models.CharField(choices=[('competition', 'Соревнование'), ('training', 'Тренировка'), ('event', 'Мероприятие')], max_length=50, verbose_name='Тип события')),
                ('discipline', models.CharField(choices=[('STREET-ART', 'STREET-ART'), ('PARKOUR', 'PARKOUR'), ('WORKOUT', 'WORKOUT'), ('БМХ', 'БМХ'), ('СКЕЙТБОРДИНГ', 'СКЕЙТБОРДИНГ'), ('ТРЮКОВОЙ САМОКАТ', 'ТРЮКОВОЙ САМОКАТ'), ('ФРИРАН', 'ФРИРАН'), ('ТРИКИНГ', 'ТРИКИНГ'), ('БРЕЙК-ДАНС', 'БРЕЙК-ДАНС'), ('ГРАФФИТИ', 'ГРАФФИТИ'), ('ДИДЖЕИНГ', 'ДИДЖЕИНГ'), ('РЕП', 'РЕП')], max_length=50, verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('coordinates', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.coordinates')),
            ],
        ),
    ]
