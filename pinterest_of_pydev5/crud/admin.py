from django.contrib import admin

from crud.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author"]
    list_display_links = ["name", "author"]
    ordering = ['-id']
    search_fields = ["name", "author"]
admin.site.register(Post, PostAdmin)
