# Generated by Django 4.2.6 on 2023-11-24 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name': 'Категория поста', 'verbose_name_plural': 'Категория постов'},
        ),
    ]
