from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from apps.home.models import Movie
from .models import Profile
from .forms import UserRegisterForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register_user(request):
    movie = Movie.objects.all()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        print(form.errors)
    return render(request, 'user/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def settings(request):
    message = ''
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user )
        if form.is_valid():
            message = "Changes were successfullyy added"
            form.save()

    else:
        form = UserChangeForm()
    return render(request, 'user/settings.html', {'form': form, 'message': message})


@login_required
def profile(request, username_slug):
    return render(request, 'user/profile.html')
