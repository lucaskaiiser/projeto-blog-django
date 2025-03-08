from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post, Category

PER_PAGE = 9


def index(request):
    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def page(request):

    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
        }
    )


def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    tags = post.tags.all()
    return render(
        request,
        'blog/pages/post.html',
        {
            "post": post,
            "tags": tags
        }
    )

def category(request, slug: str):
    posts = Post.objects.filter(category__slug=slug.lower())
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def tag(request, slug: str):
    posts = Post.objects.filter(tags__slug=slug.lower())
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def created_by(request, id: int):
    posts = Post.objects.filter(created_by=id)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )