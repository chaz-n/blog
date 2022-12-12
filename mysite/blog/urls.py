from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),

    path('about/', views.about, name='blog-about'),
    path('corey/', views.corey, name='blog-home'),

    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
