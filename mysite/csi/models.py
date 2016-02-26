from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django_markdown.models import MarkdownField

class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=50)
    content = MarkdownField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
