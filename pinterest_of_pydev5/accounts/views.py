from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User, ProfileModel
from crud.models import Post

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def userprofile(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse('404 NOT FOUND')
    user = User.objects.get(id=id)
    posts = Post.objects.filter(author=user)
    profile = ProfileModel.objects.get_or_create(user=user)
    posts_count = posts.count()
    if request.method == 'POST':
        current_user_profile = ProfileModel.objects.get(user=user)
        action = request.POST['follow']
        if action == 'unfollow':
            current_user_profile.follows.remove(profile)
        elif action == 'follow':
            current_user_profile.follows.add(profile)

        current_user_profile.save()

    context = {
        "user": user,
        "posts": posts,
        "profile": profile,
        "posts_count": posts_count
    }
    return render(request, "accounts/user_profile.html", context=context)

