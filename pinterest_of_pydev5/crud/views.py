from django.shortcuts import render
from django.views.generic import DetailView

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