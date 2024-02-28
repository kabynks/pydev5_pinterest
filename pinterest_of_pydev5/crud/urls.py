from django.urls import path

from crud.views import *
from .feeds import PostLatestFeed

urlpatterns = [
    path("", homepage, name="home"),
    path('feed/', PostLatestFeed(), name="post_feed"),

    path('tag/<int:tag_id>/',
     post_list, name='post_list_by_tag'),
    path("post/<int:id>/", post_detail, name="detail"),
    path("post/new", CreatePost.as_view(), name="post_create"),
    path('post/edit/<int:pk>/', PostEdit.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
    path("register", SignUpView.as_view(), name="signup"),
    path("about", about_view, name='about'),
    path("results/", search_view, name="search"),
    path("like/<int:id>/", like_view, name="like_view"),
]