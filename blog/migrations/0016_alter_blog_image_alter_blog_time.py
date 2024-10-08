# Generated by Django 5.0.7 on 2024-08-17 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_blog_author_alter_blog_image_alter_blog_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.URLField(default='https://www.informaticapertutti.com/wp-content/uploads/2019/02/Che_cose_un_post.webp', max_length=1000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 17, 15, 33, 2, 635518)),
        ),
    ]
