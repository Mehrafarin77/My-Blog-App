from django.contrib import admin
from .models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class BlogAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('title', 'author')
    # prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_field', 'which_post')
    list_filter = ('which_post',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comments, CommentAdmin)


