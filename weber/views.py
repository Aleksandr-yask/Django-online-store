from .forms import ProfileForm
from django.shortcuts import render
from products.models import Product
from products.models import ProductImage
from blog.models import *

# Create your views here.
def weber(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_best_sellers = products_images.filter(product__is_best_seller=True)
    products_images_new = products_images.filter(product__is_new=True)
    products_images_seller = products_images.filter(product__is_sale=True)
    products_images_top_rate = products_images.filter(product__is_top_rate=True)
    post_images = PostImage.objects.filter(is_active=True, post__is_active=True).order_by("-created")[:3]

    return render(request, 'index/index.html', locals())

