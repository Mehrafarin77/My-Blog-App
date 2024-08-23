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
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Blog(models.Model):
    title = models.CharField(max_length=112)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=dt.datetime.now())
    # slug = models.SlugField(editable=True, null=True, blank=True, default='')
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images', blank=True, null=True, default='')

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail', args=[self.pk])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    which_post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    comment_field = models.TextField()

    class Meta:
        verbose_name_plural = 'comments'
    def __str__(self):
        return self.comment_field

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     post = models.TextField()
#



