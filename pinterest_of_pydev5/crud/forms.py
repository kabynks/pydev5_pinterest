from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailField
from django.forms import *
from .models import Post

class PostForm(ModelForm):
    name = CharField(label='Name')
    description = CharField(label='Description', widget=Textarea)
    image = ImageField(label='Image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
class SignUp(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]