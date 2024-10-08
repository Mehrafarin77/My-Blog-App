# Generated by Django 5.0.7 on 2024-08-22 11:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_remove_blog_commented_by_alter_blog_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'comments'},
        ),
        migrations.AddField(
            model_name='comments',
            name='which_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 22, 15, 25, 57, 518082)),
        ),
    ]
