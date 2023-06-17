from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from user.models import Profile
from django.contrib.auth import login, logout, authenticate

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ['username']


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())