from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ['username', 'email']
