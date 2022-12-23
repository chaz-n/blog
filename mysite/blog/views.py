from django.views import generic
from .models import Post

from django.shortcuts import render

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
