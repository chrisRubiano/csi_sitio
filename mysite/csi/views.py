from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'csi/index.html', {})


def post_list(request):
    posts_list = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(posts_list, 6)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'csi/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'csi/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('csi.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'csi/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('csi.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'csi/post_edit.html', {'form': form})


def new_report(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = ReparacionForm()
    return render(request, 'csi/new_post.html', {'form': form})


