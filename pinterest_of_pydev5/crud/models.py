from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='crud-images')