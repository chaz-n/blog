from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import BlogPostForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# def home(request):
#     context = {
#         'posts': Post.objects.all(),
#     }
#     return render(request, 'blog/index.html', context)
#

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'   # <app>/<model>_<view type>.html
    context_object_name = 'posts'
    ordering = ['-created_on']
    paginate_by = 6


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'   # <app>/<model>_<view type>.html
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created_on')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogPostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = BlogPostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# class SearchListView(ListView):
#     template_name = 'blog/search_site.html'
#     model = Post
#     ordering = ['-created_on']
#     paginate_by = 6
#
#
#     def get_context_data(self, **kwargs):
#         query = self.request.GET.get('searched')
#         context = super().get_context_data(**kwargs)
#         if query:
#             context['results'] = Post.objects.filter(title__contains=query)
#             context['query'] = query
#         return context







def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched:
            is_paginated = True
        else:
            is_paginated = False
        results = Post.objects.filter(title__contains=searched)
        paginator = Paginator(results, 2)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/search_site.html',
                      {'is_paginated':is_paginated,
                       'searched': searched,
                       'results': results,
                       'page_obj': page_obj}
                      )
    else:
        return render(request, 'blog/search_site.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
