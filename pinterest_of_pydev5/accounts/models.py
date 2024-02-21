

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_image = models.ImageField(upload_to="user_images")



class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField(auto_now=True)
    bio = models.TextField(blank=True, null=True)
    follows = models.ManyToManyField("self",
    related_name='followed_by', symmetrical=False, blank=True)
    def __str__(self):
        return f"{self.user}"

