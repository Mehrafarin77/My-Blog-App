from .views import *
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', home_page_view_and_latest_posts_view, name='home'),
    path('blogs/<int:id>', post_detial, name='post_detail'),
    path('blogs/', all_posts, name='all_posts'),
    path('blogs/new', new_post, name='new_post'),
]
