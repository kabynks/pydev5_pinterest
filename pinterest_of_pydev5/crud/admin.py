from django.contrib import admin

from crud.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "slug"]
    list_display_links = ["id", "slug"]
    ordering = ['-published_date']
    search_fields = ["id", "slug"]
admin.site.register(Post, PostAdmin)
