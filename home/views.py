from django.shortcuts import render
from django.http.response import *
from .models import *


def home(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'home/home.html', context=context)


def skills(request):
    posts = Skills.objects.all()
    context = {
        'title': 'Skills',
        'posts': posts
    }
    return render(request, 'home/skills.html', context=context)


def show_my_post(request, post_id):
    return HttpResponse(f"my skill with number = {post_id}")


def login(request):
    return HttpResponse("Hello from login")


def signup(request):
    return HttpResponse("Hello from sign-up")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")
