from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User, ProfileModel
from crud.models import Post

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def userprofile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse('404 NOT FOUND')
    posts = Post.objects.filter(author=user)
    profile = ProfileModel.objects.get(user=user)
    context = {
        "user": user,
        "posts": posts,
        "profile": profile
    }
    return render(request, "accounts/user_profile.html", context=context)
