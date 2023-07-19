import datetime
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Article
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ArticleURLForm
from newspaper import Article as ArticleParser


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


def article_upload(request):

    article_form = ArticleURLForm()

    context = {
        'article_form': article_form
    }

    if request.method == "POST":
        article_form = ArticleURLForm(request.POST)
        context['article_form'] = article_form

        if article_form.is_valid():
            data = article_form.cleaned_data
            article_url = data['article_url']

            print(article_url)
            article_object = ArticleParser(article_url)
            article_object.download()
            article_object.parse()

            new_article = Article.objects.create(title=article_object.title,
                                                 url=article_url,
                                                 summary=article_object.text,
                                                 article_date=timezone.now(),
                                                 saved_on=timezone.now(),
                                                 saved_by=request.user)

    return render(request, 'article_archive/article_upload.html', context)