from django.contrib import admin

from crud.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "slug"]
    list_display_links = ["id", "slug"]
    ordering = ['-published_date']
    search_fields = ["id", "slug"]
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "created_date"]
    list_display_links = ["id", "author", "created_date"]
admin.site.register(Comment, CommentAdmin)
