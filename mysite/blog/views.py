from django.views import generic
from .models import Post

from django.shortcuts import render
from django.http import  HttpResponse


posts = [
    {
        'author': 'chaz',
        'title': 'dummy post',
        'content': 'First post content',
        'date_posted': 'Today'
    },
    {
        'author': 'chaz2',
        'title': 'dummy post2',
        'content': 'Second post content',
        'date_posted': 'Yesterday'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)
    

def about(request):
    return render(request, 'about.html', {'title': 'About'})
