from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_image = models.ImageField(upload_to="user_images")