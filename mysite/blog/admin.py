from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.action(description='Mark as published')
def make_published(ModelAdmin, request, queryset):
    queryset.update(status=1)

@admin.action(description='Mark as drafts')
def make_draft(ModelAdmin, request, queryset):
    queryset.update(status=0)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_filter = ("updated_on", "created_on", "status", "author_id")
    actions = [make_published, make_draft]


admin.site.register(Post, PostAdmin)
