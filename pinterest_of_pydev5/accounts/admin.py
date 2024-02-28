from django.contrib.admin import *
from .models import User, ProfileModel

@register(ProfileModel)
class ProfileAdmin(ModelAdmin):
    list_display = ("id", "user", "bio")
    list_display_links = ("id", "user")
    ordering = ("-id",)
class ProfileInlineAdmin(StackedInline):
    model = ProfileModel

@register(User)
class UserAdmin(ModelAdmin):
    list_display = ("id", "username", "date_joined")
    list_display_links = ("id", "username")
    ordering = ("-date_joined",)
    inlines = [ProfileInlineAdmin]

