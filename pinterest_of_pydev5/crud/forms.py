from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailField
from django.forms import *
from .models import Post

class PostForm(ModelForm):
    name = CharField(label='Name')
    description = CharField(label='Description', widget=Textarea)
    image = ImageField(label='Image')


class SignUp(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]