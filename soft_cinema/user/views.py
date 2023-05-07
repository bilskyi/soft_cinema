from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Profile
from .forms import LoginUserForm, UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'Register Form'})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Authentication Form'
        return context
    

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request, username_slug):
    return render(request, 'user/profile.html')