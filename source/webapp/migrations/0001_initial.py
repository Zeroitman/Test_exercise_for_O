# Generated by Django 2.2.2 on 2019-06-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилие пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почтовый ящик')),
                ('md5', models.TextField(verbose_name='Разделённый md5')),
                ('sha1', models.TextField(verbose_name='Разделённый sha1')),
                ('sha256', models.TextField(verbose_name='Разделённый sha256')),
                ('all_user_data', models.TextField(verbose_name='Все полученные данные')),
            ],
        ),
    ]
