from .views import *
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog-home'),

]
