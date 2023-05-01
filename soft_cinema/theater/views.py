from django.shortcuts import render

def theater(request):
    return render(request, 'theater/theater.html')