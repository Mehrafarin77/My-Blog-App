# Generated by Django 5.0.7 on 2024-07-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Blog Title', max_length=112)),
                ('content', models.TextField()),
                ('image', models.URLField(default='https://www.informaticapertutti.com/wp-content/uploads/2019/02/Che_cose_un_post.webp')),
            ],
        ),
    ]
