from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.user.models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ['username', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email']