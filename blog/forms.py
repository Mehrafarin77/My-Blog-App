from django.forms import ModelForm
from.models import *

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'time', 'image']