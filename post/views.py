from django.shortcuts import render, redirect

from post.forms import PostForm, CategoryForm, CommentForm
from post.models import Post, Category, Comment


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    posts = Post.objects.all()
    ctx = {
        'posts': posts,
        'post_form': PostForm(),
        'cats': Category.objects.all(),
        'cat_form': CategoryForm(),
    }

    return render(request, 'post/index.html', ctx)


def post_info(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=id)
            comment.save()

    post = Post.objects.get(pk=id)
    comments = post.comments.all()

    ctx = {
        'post': post,
        'comment_form': CommentForm(),
        'comments': comments,
        'post_form': PostForm(),
    }

    return render(request, 'post/post_info.html', ctx)


def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()

    return redirect('index')


def edit_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

    return redirect('post_info', id=post.id)


def comment_delete(request, id):
    comment = Comment.objects.get(pk=id)
    comment.delete()

    return redirect('post_info',  id=comment.post.id)


def cat_info(request, id):
    cat = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()

    ctx = {
        'cat': cat,
        'posts': Post.objects.filter(category=cat),
        'cat_form': CategoryForm(),
    }
    return render(request, 'post/cat_info.html', ctx)


def cat_delete(request, id):
    cat = Category.objects.get(pk=id)
    cat.delete()

    return redirect('index')


def add_cat(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('index')
