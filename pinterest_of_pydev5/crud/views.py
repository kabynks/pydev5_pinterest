
from django.contrib.auth.mixins import LoginRequiredMixin
from taggit.models import Tag
from django.db.models import Count

from django.http import HttpResponseRedirect
from .forms import SearchForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView, UpdateView, DeleteView
)
from .forms import SignUp
from crud.models import Post, LikePost
from django.views.decorators.cache import cache_page

@cache_page(20)
def homepage(request):

    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "crud/home.html", context=context)

def post_list(request, tag_id=None):
    tag = None
    object_list = Post.objects.all()
    if tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        object_list = object_list.filter(tag__in=[tag])
    context = {
        "tag": tag,
        "posts": object_list
    }

    return render(request, "crud/post_list_tags.html", context=context)
def post_detail(request, id):
    post = Post.objects.get(id=id)
    post_tags = post.tag.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tag__in=post_tags) \
    .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tag=Count("tag")) \
    .order_by("-same_tag", )
    context = {
        'post': post,
        'similar_posts': similar_posts,

    }
    return render(request, 'crud/detail_post.html', context)

from django.urls import reverse

def like_view(request, id):
    user = request.user
    if request.method == 'POST':
        post_obj = Post.objects.get(id=id)
        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like,created = LikePost.objects.get_or_create(user=user, post=post_obj)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    detail_url = reverse('detail', args=[id])
    return redirect(detail_url)



class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "crud/post_create.html"
    success_url = reverse_lazy("home")
    fields = ["name", "description", "image", "tag"]
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



