from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import *
from .forms import *


def frontpage(request):
    posts = Post.objects.filter(is_published=True)
    context = {
        'posts': posts,
    }
    return render(request, 'core/frontpage.html', context)


def about(request):
    return render(request, 'core/about.html')


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', slug=slug, category_slug=category_slug)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'core/detail.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(is_published=True)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'core/category_list.html', context)


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(is_published=True).filter(Q(title__icontains=query) | Q(body__icontains=query))
    context = {
        'posts': posts,
        'query': query,
    }

    return render(request, 'core/search.html', context)


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")


