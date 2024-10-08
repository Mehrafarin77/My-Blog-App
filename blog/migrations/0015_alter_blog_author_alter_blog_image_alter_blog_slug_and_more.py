# Generated by Django 5.0.7 on 2024-08-17 12:02

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_blog_slug_alter_blog_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.URLField(default='https://www.informaticapertutti.com/wp-content/uploads/2019/02/Che_cose_un_post.webp', max_length=256),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 17, 15, 32, 5, 868881)),
        ),
    ]
