# Generated by Django 4.2.2 on 2023-06-20 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Пользователи'},
        ),
    ]