import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy, reverse
from .models import Post

class PostLatestFeed(Feed):
    title = "Posts"
    link = reverse_lazy("home")
    description = "New posts"
    def items(self):
        return Post.objects.order_by('-published_date')[:5]
    def item_title(self, item):
        return item.name
    def item_description(self, item):
        return truncatewords(markdown.markdown(item.description), 30)

    def item_published(self, item):
        return item.published_date

    def item_link(self, item):
        return reverse('detail', args=[item.slug])
