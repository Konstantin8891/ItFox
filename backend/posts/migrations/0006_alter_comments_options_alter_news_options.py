# Generated by Django 4.2.2 on 2023-06-21 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_comments_author_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Коментарии'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Новости'},
        ),
    ]
