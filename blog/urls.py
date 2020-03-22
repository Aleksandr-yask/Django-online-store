from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('post/<post_id>/', views.post_id, name = 'post_id'),
    path('tags/<tag_id>', views.tag_id, name = 'tag_id')

]
