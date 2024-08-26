from .views import *
from django.urls import path
from django.http import Http404

app_name = 'blog'
urlpatterns = [
    path('posts/favorite/', FavoriteView.as_view(), name='favorite'),
    path('posts/readlater/', ReadLaterView.as_view(), name='readlater'),
    path('single-post/all-comments/<int:pk>/', AllCommentsView.as_view(), name='all-comments'),
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
    path('logout/', logout, name='logout'),
    path('profiles/', UserProfileView.as_view(), name='userprofile'),
    path('search/', SearchView.as_view(), name='search')

]