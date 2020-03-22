from django.shortcuts import render
from blog.models import *
from products.models import ProductImage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def blog(request):
    post_images = PostImage.objects.filter(is_active=True, post__is_active=True).order_by('-created').all()
    post_tags = TagsPost.objects.filter(is_active=True)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)[:5]
    tags = Tags.objects.filter(is_active=True)
    paginator = Paginator(post_images, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    vars = dict(
        posts=posts,
        )
    return render(request, 'blog/blog.html', locals(), vars)

# ======================================================================================================

def post_id(request, post_id):
    post = Post.objects.get(id=post_id)
    post_images = PostImage.objects.filter(is_active=True, post__is_active=True, post__id = post_id)
    post_tags = TagsPost.objects.filter(is_active=True, tag_post_id = post_id)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)[:5]
    tags = Tags.objects.filter(is_active=True)

    return render(request, 'blog/blog-detail.html', locals())

# ======================================================================================================

def date_post(request, month_post, year_post):
    post_images = PostImage.objects.filter(is_active=True, post__is_active=True, post__update__month=month_post, post__update__year=year_post)
    post_tags = TagsPost.objects.filter(is_active=True)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)[:5]
    tags = Tags.objects.filter(is_active=True)
    archive = PostImage.objects.filter(is_active=True, post__is_active=True)

    return render(request, 'blog/blog.html', locals())

# ======================================================================================================

def tag_id(request, tag_id):
    post_images = PostImage.objects.filter(is_active=True, post__is_active=True, post__tagspost__tag_name_id=tag_id).order_by('-created').all()
    post_tags = TagsPost.objects.filter(is_active=True)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)[:5]
    tags = Tags.objects.filter(is_active=True)
    paginator = Paginator(post_images, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    vars = dict(
        posts=posts,
    )
    return render(request, 'blog/blog.html', locals(), vars)


