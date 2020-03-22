from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('', views.products, name = 'products'),
    path('product/<product_id>/', views.product, name = 'product'),
    path('category/<product_category>/', views.product_category, name = 'product_category'),
    path('search/', views.product_search, name = 'product_search'),
    path('accessories/<product_id>/', views.accessories_products, name = 'accessories'),
    path('clothing/<product_id>/', views.clothing_products, name = 'clothing'),
    path('accesories/', views.accessories, name = 'accessories'),
    path('price/', views.price_sort, name = 'price_sort'),
    path('sale/', views.sale, name = 'sale'),
    path('<sex>/', views.sex, name = 'sex'),

    # path('accesories/', views.accessories, name = 'accessories'),
    # path('sale/', views.sale, name = 'sale'),
    # url(r'^u/(?P<id>\w+)/$', views.products, name = 'product')
]

