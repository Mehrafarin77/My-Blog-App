# Generated by Django 5.0.7 on 2024-08-23 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_blog_author_comments_user_alter_blog_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 23, 23, 53, 5, 332415)),
        ),
    ]
