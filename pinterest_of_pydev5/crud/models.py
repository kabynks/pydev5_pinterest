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

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.published_date


