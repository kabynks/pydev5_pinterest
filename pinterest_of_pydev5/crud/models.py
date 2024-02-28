from django.contrib.sitemaps import Sitemap

from django.urls import reverse

from accounts.models import User
from django.db import models
from autoslug import AutoSlugField


from taggit.managers import TaggableManager

class Post(models.Model):
    tag = TaggableManager()

    name = models.CharField(max_length=150)

    description = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='crud-images')
    slug = AutoSlugField(
        populate_from='name',
        editable=False,
        blank=True,
    )
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='likes')
    def __str__(self):
        return self.slug

    @property
    def num_likes(self):
        return self.likes.all.count()
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.published_date
LIKE_CHOISES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)
class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")
    value = models.CharField(choices=LIKE_CHOISES, default='Like', max_length=10)



