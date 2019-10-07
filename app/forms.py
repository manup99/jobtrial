from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
class UserForm(UserCreationForm):
    email=forms.CharField(widget=forms.EmailInput)
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','email','password1','password2']

