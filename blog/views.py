from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.filter(published=True)[:3]
    return render(request, 'blog/home.html', {'posts': posts})

def blog_index(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
