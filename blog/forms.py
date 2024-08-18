from django.forms import ModelForm
from.models import *

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'image', 'slug', 'tags']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['caption']