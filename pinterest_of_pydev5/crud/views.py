from django.shortcuts import render, redirect
from django.views.generic import (
    DetailView,
    CreateView
)
from .forms import PostForm
from crud.models import Post
from django.urls import reverse_lazy


def homepage(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "crud/home.html", context=context)
class PostDetail(DetailView):
    model = Post
    template_name = "crud/detail_post.html/"
    context_object_name = 'post'

def PostCreate(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'crud/post_create.html', context=context)

def PostEdit(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(commit=True)
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'crud/post_edit.html', context=context)

def PostDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('home')

