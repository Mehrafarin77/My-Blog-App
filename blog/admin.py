from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'text')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Author, AuthorAdmin)
