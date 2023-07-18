from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    summary = models.TextField()
    article_date = models.DateTimeField()
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_articles')
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
