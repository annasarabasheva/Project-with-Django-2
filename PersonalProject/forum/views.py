from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from PersonalProject.forum.forms import PostForm, CategoryForm
from PersonalProject.forum.models import Category, Thread, Post, Like


def forum_home(request):
    categories = Category.objects.all()
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_home')

    return render(request, 'forum/forum-home.html', {'categories': categories, 'form': form})


def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    threads = category.threads.all()
    return render(request, 'forum/category.html', {'category': category, 'threads': threads})


def thread_view(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    posts = Post.objects.filter(thread=thread)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('thread_view', thread_id=thread.id)
    else:
        form = PostForm()

    return render(request, 'forum/thread.html', {
        'thread': thread,
        'posts': posts,
        'form': form
    })


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    existing_like = Like.objects.filter(user=request.user, post=post).first()

    if existing_like:
        existing_like.delete()
    else:
        Like.objects.create(user=request.user, post=post)

    return redirect('thread_view', thread_id=post.thread.id)


def create_post(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        post = Post.objects.create(thread=thread, content=content, created_by=request.user)
        return redirect('thread_view', thread_id=thread.id)
    return render(request, 'forum/create-post.html', {'thread': thread})