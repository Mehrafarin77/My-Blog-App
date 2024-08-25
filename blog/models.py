from django.db import models
import datetime as dt
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
        return self.caption

class Author(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Blog(models.Model):
    title = models.CharField(max_length=112)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=dt.datetime.now())
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images', blank=True, null=True, default='')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.title}'

class Comments(models.Model):
    user_name = models.CharField(max_length=50, null=True)
    user_email =  models.EmailField(null=True)
    text = models.TextField(null=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return  f'{self.text} (id: {self.pk})'