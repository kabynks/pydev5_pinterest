from django.contrib import admin

from crud.models import Post, LikePost


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "slug"]
    list_display_links = ["id", "slug"]
    ordering = ['-published_date']
    search_fields = ["id", "slug"]
admin.site.register(Post, PostAdmin)

class LikePostAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "user"]
    list_display_links = ["id", "post", "user"]
    ordering = ['-id']
admin.site.register(LikePost, LikePostAdmin)