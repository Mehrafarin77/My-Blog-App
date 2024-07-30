from django.db import models
import datetime as dt

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=112, default='Blog Title')
    content = models.TextField()
    author = models.CharField(max_length=112 ,default='unknown')
    time = models.DateTimeField(default=dt.datetime.now().strftime('%Y-%m-%d'))
    image = models.URLField(default='https://www.informaticapertutti.com/wp-content/uploads/2019/02/Che_cose_un_post.webp')

    def __str__(self):
        return self.title