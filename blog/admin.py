from django.contrib import admin
from .models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class BlogAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
