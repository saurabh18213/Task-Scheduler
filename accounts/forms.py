from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = User
        fields = ('username', 'image', 'password1', 'password2')
