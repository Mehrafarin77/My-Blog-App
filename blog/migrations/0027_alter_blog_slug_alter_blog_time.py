# Generated by Django 5.0.7 on 2024-08-21 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_blog_slug_alter_blog_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 21, 13, 21, 34, 717283)),
        ),
    ]
