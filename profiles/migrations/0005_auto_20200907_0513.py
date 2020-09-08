# Generated by Django 3.1 on 2020-09-07 04:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20200825_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='avatar'),
        ),
    ]
