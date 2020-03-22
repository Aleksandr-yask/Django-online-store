from .models import ProductInBasket


def basket_reload(request):
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()


    products_in_basket =  ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    total_nmb = products_in_basket.count()
    return locals()


