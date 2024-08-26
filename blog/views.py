from django.shortcuts import render, redirect
from django.urls import path, reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView, View

# Create your views here.
class PostsView(ListView):
    model = Blog
    template_name = 'all_posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fav_post = Blog.objects.filter(pk=self.request.session.get('favorite_post'))
        read_later = Blog.objects.filter(pk=self.request.session.get('read_later'))
        context['fav_post'] = fav_post[0].id if fav_post else None
        context['read_later'] = read_later[0].id if read_later else None
        return context

class SinglePostView(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_favorite'] = str(self.object.id) == str(self.request.session.get('favorite_post'))
        context['is_read_later'] = str(self.object.id) == str(self.request.session.get('read_later'))
        return context


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

class NewTagView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'new_tag.html'
    success_url = reverse_lazy('blog:new_post')


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


class CommentView(View):
    def get(self, request, pk):
        comment_form = CommentForm()
        post = Blog.objects.get(pk=pk)
        context = {
            'post':post,
            'form':comment_form
        }
        return render(request, 'comment.html', context)
    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        post = Blog.objects.get(pk=pk)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect('/single-post/all-comments/' + str(pk))
        return render(request, 'comment.html', {
            'post':post,
            'form':comment_form
        })


class AllCommentsView(ListView):
    template_name = 'all-comments.html'
    model = Comments
    def get_context_data(self, **kwargs):
        related_comments = []
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs['pk']
        post = Blog.objects.get(pk=post_id)
        comments = Comments.objects.all()
        for comment in comments:
            if comment.post:
                if comment.post.pk == post_id:
                    related_comments.append(comment)
        context['comments'] = related_comments[::-1]
        context['post'] = post
        return context


def logout(request):
    return render(request, 'registration/logout.html')

class UserProfileView(TemplateView):
    template_name = 'userprofile.html'

class FavoriteView(View):
    def post(self, request):
        post_id = request.POST['post_id']
        request.session['favorite_post'] = post_id
        return HttpResponseRedirect('/single-post/' + post_id)

class ReadLaterView(View):
    def post(self, request):
        post_id = request.POST['post_id']
        request.session['read_later'] = post_id
        return HttpResponseRedirect('/single-post/' + post_id)


class NewAuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'new_author.html'
    success_url = reverse_lazy('blog:new_post')


class SearchView(View):
    def post(self, request):
        content = request.POST['search']
        posts = Blog.objects.filter(title__contains= content) | Blog.objects.filter(content__contains=content)
        print(posts)
        return render(request, 'all_posts.html', {
            'posts': posts
        })













