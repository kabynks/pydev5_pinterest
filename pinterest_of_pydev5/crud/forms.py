from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

from django.forms import *




class PostForm(ModelForm):
    name = CharField(label='Name')
    description = CharField(label='Description', widget=Textarea)
    image = ImageField(label='Image')


class SignUp(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "user_image", "password1", "password2"]


class SearchForm(Form):
    query = CharField(label='Search', widget=Textarea)
