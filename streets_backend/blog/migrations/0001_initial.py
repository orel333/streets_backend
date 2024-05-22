<<<<<<< HEAD
# Generated by Django 4.2.7 on 2024-05-22 09:45
=======
# Generated by Django 5.0.6 on 2024-05-16 19:49
>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
<<<<<<< HEAD
                ('image', models.ImageField(upload_to='blogs/images/', verbose_name='Картинка')),
                ('type', models.CharField(choices=[('post', 'Пост'), ('news', 'Новость')], default='post', max_length=4, verbose_name='Тип поста')),
                ('relevance_date', models.DateField(verbose_name='Крайняя дата актуальности новости')),
            ],
            options={
                'verbose_name': 'Пост блога',
                'verbose_name_plural': 'Посты блога',
            },
        ),
        migrations.CreateModel(
            name='PostRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutus.region')),
=======
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)
            ],
            options={
                'verbose_name': 'Пост блога',
                'verbose_name_plural': 'Посты блога',
            },
        ),
    ]
