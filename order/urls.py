from django.contrib import admin
from django.urls import path
from products import views
from order import views

urlpatterns = [
    path('', views.cart, name = 'cart'),
    path('add/', views.add_to_cart, name = 'product_id'),
    path('delete/', views.delete, name = 'delete'),
    path('add_image/<id>', views.add_image, name = 'add_image'),
    # path('reload_basket/', views.reload_basket, name = 'reload_basket')
]
