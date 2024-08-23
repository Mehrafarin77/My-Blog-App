from .views import *
from django.urls import path
from django.http import Http404

app_name = 'blog'
urlpatterns = [
    path('single-post/<slug:slug>/all-comments/', allcomments, name='all-comments'),
    path('single-post/<int:pk>/comment/', CommentView.as_view(), name='comment'),
    path('posts/tags/<slug:slug>/', allpostwithsametags, name='all_posts_with_same_tags'),
    path('single-post/<int:pk>/', SinglePostView.as_view(), name='post_detail'),  # blogs/my-first-blog
    path('posts/', PostsView.as_view(), name='posts'),
    path('', LatestPostsView.as_view(), name='latest_posts'),
    path('posts/delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('posts/update/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('new-post/', NewPostView.as_view(), name='new_post'),
    path('new-author/', NewAuthorView.as_view(), name='new_author'),
    path('new-tag/', NewTagView.as_view(), name='new_tag'),
    path('logout/', logout, name='logout')

]