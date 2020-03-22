from django.contrib import admin
from django.urls import path
from blog import views
from django.urls import path
from about import views

urlpatterns = [
    path('', views.about, name = 'about'),

]
