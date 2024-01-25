from django.urls import path

from crud.views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("post/<int:pk>/", PostDetail.as_view(), name="detail"),
    path("post/new/", CreatePost.as_view(), name="post_create"),
    path('post/edit/<int:pk>/', PostEdit.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
    path("register", SignUpView.as_view(), name="signup"),
    path("about", about_view, name='about')
]