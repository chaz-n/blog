
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget()
        }