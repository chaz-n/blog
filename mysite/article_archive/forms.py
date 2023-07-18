from django import forms
from .models import Article


class ArticleURLForm(forms.Form):
    article_url = forms.CharField(label='URL Address for Article')

