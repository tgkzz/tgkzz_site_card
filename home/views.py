from django.shortcuts import render
from django.http.response import *
from .models import *


def home(request):
    return render(request, 'home/home.html', {'title': 'Home Page'})


def skills(request):
    posts = Skills.objects.all()
    return render(request, 'home/skills.html', {'posts': posts})


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")