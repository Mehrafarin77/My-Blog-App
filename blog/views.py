from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from .models import *
from .forms import *


# Create your views here.
def home_page_view_and_latest_posts_view(request):
    blogs = Blog.objects.all()
    latest = blogs[len(blogs) - 3: ]
    context = {
        'latest': latest
    }
    return render(request, 'home_page.html', context)


def post_detial(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, 'detail.html', context)


def all_posts(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'all_posts.html', context)


def new_post(request):
    form = BlogForm(request.POST)
    if request.method == "POST":
        form = BlogForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = BlogForm()

    return render(request, 'new_post.html', {'form': form})




