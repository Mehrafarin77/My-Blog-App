from django import forms
from.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['caption']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['post']
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'text': 'Your Comment'
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'firstname': 'Your first name',
            'lastname': 'Your last name',
        }


