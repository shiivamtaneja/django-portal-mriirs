from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
