from django import forms
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=MarkdownWidget())
    #content2 = MarkdownFormField()
