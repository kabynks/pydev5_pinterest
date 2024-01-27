from django.urls import path

from crud.views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("post/<slug:slug>/", PostDetail.as_view(), name="detail"),
    path("post/new", CreatePost.as_view(), name="post_create"),
    path('post/edit/<slug:slug>/', PostEdit.as_view(), name='post_edit'),
    path('post/delete/<slug:slug>/', PostDelete.as_view(), name='post_delete'),
    path("register", SignUpView.as_view(), name="signup"),
    path("about", about_view, name='about'),
    path("results/", search_view, name="search")
]