from django.urls import path

from crud.views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("post/<int:pk>/", PostDetail.as_view(), name="detail")
]