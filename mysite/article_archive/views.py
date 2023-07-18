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
    template_name = 'article_archive/index.html'   # <app>/<model>_<view type>.html
    context_object_name = 'articles'
    ordering = ['-saved_on']
    paginate_by = 6


class ArticleDetailView(DetailView):
    model = Article


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/article-archive'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.saved_by:
            return True
        return False