from django.shortcuts import render
from .models import Article
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/index.html'   # <app>/<model>_<view type>.html
    context_object_name = 'articles'
    ordering = ['-saved_on']
    paginate_by = 6

    def get_queryset(self):
        articles = super().get_queryset()
        return

