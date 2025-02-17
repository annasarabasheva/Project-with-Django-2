from django.shortcuts import render, get_object_or_404, redirect

from PersonalProject.forum.forms import PostForm
from PersonalProject.forum.models import Category, Thread, Post


def forum_home(request):
    categories = Category.objects.all()
    return render(request, 'forum/forum-home.html', {'categories': categories})


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


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('thread_view', thread_id=post.thread.id)


def create_post(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        post = Post.objects.create(thread=thread, content=content, created_by=request.user)
        return redirect('thread_view', thread_id=thread.id)
    return render(request, 'forum/create-post.html', {'thread': thread})