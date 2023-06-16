from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import Profile

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ['username', 'password']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())