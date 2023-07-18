from .views import *
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-home'),
    path('upload', article_upload, name='article-upload'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete'),

]
