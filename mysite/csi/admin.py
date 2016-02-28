from django.contrib import admin
from .models import Post
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
admin.site.register(Post, MarkdownModelAdmin)
