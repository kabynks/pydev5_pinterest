from django.contrib.admin import *
from .models import User

@register(User)
class UserAdmin(ModelAdmin):
    list_display = ("id", "username", "date_joined")
    list_display_links = ("id", "username")
    ordering = ("-date_joined",)

