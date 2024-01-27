from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
import uuid
class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4,)
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