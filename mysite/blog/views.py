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


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def corey(request):
    context = {
        'posts': posts
    }
    return render(request, 'test.html', context)
    

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
