from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def movies(request):
    return render(request, 'home/movies.html')