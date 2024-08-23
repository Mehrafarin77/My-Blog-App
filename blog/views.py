from django.shortcuts import render, redirect
from django.urls import path, reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
class PostsView(ListView):
    model = Blog
    template_name = 'all_posts.html'
    context_object_name = 'posts'

class SinglePostView(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'post'


class LatestPostsView(ListView):
    model = Blog
    template_name = 'home_page.html'
    context_object_name = 'latest_posts'
    ordering = ['-time']

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        latest_posts = queryset[:3]
        return latest_posts

class NewPostView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'new_post.html'
    success_url = '/posts'
    context_object_name = 'form'

class DeletePostView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:posts')
    template_name = 'confirm.html'

class UpdatePostView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'new_post.html'
    success_url = reverse_lazy('blog:posts')

class NewAuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'new_author.html'
    success_url = reverse_lazy('blog:new_post')

class NewTagView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'new_tag.html'
    success_url = reverse_lazy('blog:new_post')

# class AllPostsWithSameTagsView(ListView):
#     model = Blog
#     template_name = 'all_posts_with_same_tags.html'
#     context_object_name = 'posts'
#
#     def get_queryset(self, **kwargs):
#         blogs = []
#         context = super().get_queryset(**kwargs)
#         for blog in context:
#             for tag in blog.tags.all():
#                 if str(tag).lower() == self.kwargs.get('slug'):
#                     blogs.append(blog)
#         return blogs

def allpostwithsametags(request, slug):
    posts = Blog.objects.all()
    same_posts = []
    for post in posts:
        for tag in post.tags.all():
            if str(tag).lower() == slug.lower():
                print(tag)
                same_posts.append(post)

    context = {
        'posts':same_posts,
        'tag': slug
    }
    return render(request, 'all_posts_with_same_tags.html', context)


class CommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'comment.html'
    success_url = reverse_lazy('blog:posts')
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.kwargs.get('pk')
        return context


def allcomments(request, slug):
    all_comments = []
    comments = Comments.objects.all()
    for comment in comments:
        if str(comment.which_post).title() == str(slug).title():
            all_comments.append(comment)
    return render(request, 'all-comments.html', {
        'comments': all_comments,
        'slug': slug
    })


def logout(request):
    return render(request, 'registration/logout.html')




