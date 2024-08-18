from .views import *
from django.urls import path
from django.http import Http404

app_name = 'blog'
urlpatterns = [
    path('posts/<slug:slug>', post_detail, name='post_detail'),  # blogs/my-first-blog
    path('posts/', posts, name='posts'),
    path('', latest_posts, name='latest_posts'),
    path('posts/delete/<slug:slug>/', delete_post, name='delete_post'),
    path('posts/update/<slug:slug>/', update_post, name='update_post'),
    path('new-post/', new_post, name='new_post'),
    path('new-author/', new_author, name='new_author'),
    path('new-tag/', new_tag, name='new_tag'),
]