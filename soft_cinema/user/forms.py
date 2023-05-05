from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
