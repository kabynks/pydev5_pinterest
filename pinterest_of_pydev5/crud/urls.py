from django.urls import path

from crud.views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("post/<int:pk>/", PostDetail.as_view(), name="detail"),
    path("post/new/", PostCreate, name="post_create"),
    path('post/edit/<int:pk>/', PostEdit, name='post_edit'),
    path('post/delete/<int:pk>/', PostDelete, name='post_delete'),
]