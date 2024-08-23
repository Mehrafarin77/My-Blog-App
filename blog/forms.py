from django import forms
from.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['caption']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        labels = {
            'which_post': 'For which post',
            'comment_field': 'comment'
        }




