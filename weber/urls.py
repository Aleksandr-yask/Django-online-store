from django.contrib import admin
from django.urls import path
from weber import views

urlpatterns = [
    path('', views.weber, name = 'weber')
]
