from django.shortcuts import render
from products.models import Product
from products.models import ProductImage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def products(request):
    sort = request.GET.get('sort')
    if sort == None or sort == 'def' or sort == "None":
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by('-product__importance')

        paginator = Paginator(products_images, 12)
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

        return render(request, 'product/shop.html', locals())

    elif sort == 'lowth':
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by(
            'product__product_price')

        paginator = Paginator(products_images, 12)
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

        return render(request, 'product/shop.html', locals())


    elif sort == 'htlow':
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by(
            '-product__product_price')

        paginator = Paginator(products_images, 12)
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

        return render(request, 'product/shop.html', locals())




    # ======================================================================================================

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product_id=product_id)
    products_related = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)

    return render(request, 'products/product.html', locals())


    # ======================================================================================================

def sex(request, sex):
    sort = request.GET.get('sort')
    if sort == None or sort == 'def' or sort == "None":
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__sex=sex).order_by(
            '-product__importance')

        paginator = Paginator(products_images, 12)
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

        return render(request, 'product/shop.html', locals())

    elif sort == 'lowth':
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__sex=sex).order_by(
            'product__product_price')

        paginator = Paginator(products_images, 12)
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

        return render(request, 'product/shop.html', locals())


    elif sort == 'htlow':
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__sex=sex).order_by(
            '-product__product_price')

        paginator = Paginator(products_images, 12)
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

        return render(request, 'product/shop.html', locals())

    # ======================================================================================================

def accessories(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__product_class=4).order_by('-product__importance')
    paginator = Paginator(products_images, 12)
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

    return render(request, 'products/product_accessories.html', locals())

    # ======================================================================================================

def sale(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__is_sale=True).order_by('-product__importance')
    paginator = Paginator(products_images, 12)
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

    return render(request, 'product/shop.html', locals())


    # ======================================================================================================

def accessories_products(request, product_id):
    product = Product.objects.get(id=product_id)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__product_class=4).order_by('-product__importance')
    paginator = Paginator(products_images, 12)
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

    return render(request, 'products/product_accessories.html', locals())

    # ======================================================================================================

def clothing_products(request, product_id):
    product = Product.objects.get(id=product_id)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__product_class=2)
    paginator = Paginator(products_images, 12)
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

    return render(request, 'product/product_clothing.html', locals())

    # ======================================================================================================

def product_category(request, product_category):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__product_category_id=product_category)
    paginator = Paginator(products_images, 12)
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

    return render(request, 'product/shop.html', locals())

    # ======================================================================================================

def product_search(request,  *args, **kwargs):
    question = request.GET.get('q')
    if len(question) < 100:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__product_name__contains = question).order_by('-product__importance')
        if len(products_images) > 0:
            paginator = Paginator(products_images, 12)
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
        else:
            not_find = True
    else:
        max_lenght = True


    return render(request, 'product/shop.html', locals())

    # ======================================================================================================

def add_to_cart(request, product_id):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__id=product_id)

    return True

    # ======================================================================================================

def price_sort(request, *args, **kwargs):
    price_min = request.GET.get('min')
    price_max = request.GET.get('max')
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__product_price__gte = price_min,
                                                  product__product_price__lte = price_max)
    paginator = Paginator(products_images, 12)
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

    return render(request, 'product/shop.html', locals())

    # ======================================================================================================

