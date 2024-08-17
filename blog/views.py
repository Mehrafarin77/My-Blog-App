from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from .models import *
from .forms import *

# Create your views here.

def posts(request):
    try:
        posts = Blog.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'all_posts.html', context)
    except:
        raise Http404()


def post_detail(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        return render(request, 'detail.html', {'blog': blog})
    except:
        raise Http404()


def latest_posts(request):
    posts = Blog.objects.all()
    latest_posts = posts[:3]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'home_page.html', context)


def new_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:posts')
    else:
        form = BlogForm()
    return render(request, 'new_post.html', {'form':form})


def delete_post(request, slug):
    post = Blog.objects.get(slug=slug)
    post.delete()
    return redirect('blog:posts')

def update_post(request, slug):
    post = Blog.objects.get(slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:posts')
    else:
        form = BlogForm(instance=post)
    return render(request, 'new_post.html', {'form':form})











