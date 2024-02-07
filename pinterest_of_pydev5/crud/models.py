from accounts.models import User
from django.db import models
from autoslug import AutoSlugField

from django.utils import timezone
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



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
