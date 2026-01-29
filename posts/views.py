from django.shortcuts import render
from django.db.models import Q 
from .models import Category, Post, Author
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def homepage (request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'homepage.html',context)

def post (request,slug):
    post = Post.objects.get(slug = slug)
    latest = Post.objects.order_by('-timestamp')[:3]
    context={
        'post': post,
        'latest': latest,
        
    }            
    return render(request, 'post.html', context)

def about (request):
    return render(request, 'about_page.html')

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'object_list': queryset
    }
    return render(request, 'search_bar.html', context)


def postlist (request,slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)

def allposts(request):
    posts = Post.objects.order_by('-timestamp')

    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)



@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)   # UNLIKE
        liked = False
    else:
        post.likes.add(user)      # LIKE
        liked = True

    return JsonResponse({
        'liked': liked,
        'total_likes': post.likes.count()
    })
