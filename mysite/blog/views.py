from django.views import generic
from .models import Post

from django.shortcuts import render


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
    return render(request, 'blog/index.html', context)
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
