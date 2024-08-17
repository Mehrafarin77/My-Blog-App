from django.db import models
import datetime as dt
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Blog(models.Model):
    title = models.CharField(max_length=112, default='Blog Title')
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=dt.datetime.now())
    image = models.URLField(max_length=1000, default='https://www.informaticapertutti.com/wp-content/uploads/2019/02/Che_cose_un_post.webp')
    slug = models.SlugField(editable=True, db_index=True, default='', null=False, blank=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'