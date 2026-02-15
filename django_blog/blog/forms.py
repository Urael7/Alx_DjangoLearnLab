from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post


# Blog Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


# Registration Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# Profile Update Form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
