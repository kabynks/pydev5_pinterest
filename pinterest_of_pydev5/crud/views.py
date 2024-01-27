from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import SearchForm

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView, UpdateView, DeleteView,

)
from .forms import PostForm, SignUp
from crud.models import Post



def homepage(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "crud/home.html", context=context)
class PostDetail(DetailView):
    model = Post
    template_name = "crud/detail_post.html/"
    context_object_name = 'post'

class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "crud/post_create.html"
    success_url = reverse_lazy("home")
    fields = ["name", "description", "image"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEdit(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "crud/post_edit.html"
    fields = ["name",
        "description",
        "image"
    ]
    context_object_name = "post"
    success_url = reverse_lazy("home")


class PostDelete(DeleteView):
    model = Post
    template_name = "crud/post_delete.html"
    success_url = reverse_lazy("home")
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    form_class = SignUp
def about_view(request):
    return render(request, "crud/about.html")
def search_view(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        q = form.cleaned_data["query"]
        results = Post.objects.filter(name__icontains=q)
    context = {
        "form": form,
        "results": results
    }
    return render(request, "crud/search_post.html", context=context)
