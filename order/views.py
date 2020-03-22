from django.shortcuts import render
from products.models import *
from django.http import JsonResponse, HttpResponse
from .models import ProductInBasket, ProductImage
# Create your views here.




def add_to_cart(request):
    return_dict = dict()
    session_key = request.session.session_key
    id = request.GET.get('id')
    nmb = request.GET.get('number')
    img = request.GET.get('img')
    new_product, created_product = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=id, defaults={'nmb':nmb, 'img': img})
    if not created_product:
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)


    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    total_nmb = products_in_basket.count()

    return_dict["total_nmb"] = total_nmb

    return_dict["products"] = list()
    for item in products_in_basket:
        product_dict = dict()
        product_dict["name"] = item.product.product_name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        product_dict["id"] = item.id
        product_dict["img"] = item.img
        product_dict["product_id"] = item.product_id
        return_dict["products"].append(product_dict)

    # products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__id=id)
    return JsonResponse(return_dict)


    # ======================================================================================================

def add_image(request, id):
    images_in_basket = ProductImage.objects.filter(is_active=True, is_main=True, product_id = id)

    return render(request, 'base/basket.html', locals())

def cart(request):

    return render(request, 'cart/cart.html', locals())

    # ======================================================================================================
def delete(request):
    id = request.GET.get('id')
    session_key = request.session.session_key

    try:
        person = ProductInBasket.objects.get(session_key=session_key, id=id)
        person.delete()
        products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
        total_nmb = products_in_basket.count()

        return_dict = dict()
        return_dict["total_nmb"] = total_nmb

        return_dict["products"] = list()
        for item in products_in_basket:
            product_dict = dict()
            product_dict["name"] = item.product.product_name
            product_dict["price_per_item"] = item.price_per_item
            product_dict["nmb"] = item.nmb
            product_dict["id"] = item.id
            product_dict["img"] = item.img
            product_dict["product_id"] = item.product_id
            return_dict["products"].append(product_dict)

        return JsonResponse(return_dict)
    except ProductInBasket.DoesNotExist:
        return HttpResponse("<h2>Person not found</h2>")