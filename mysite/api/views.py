from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Post.objects.all()
        return posts.filter(status=1)



class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Post.objects.all()
        return posts.filter(status=1)