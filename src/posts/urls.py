from django.contrib import admin
from django.urls import path, include
from posts.views import posts_list, posts_delete, post_create, post_detail, posts_update

from . import views

urlpatterns = [ 
    path('^$/', "post_list"),
    path('create/', "post_create"), 
    path('detail/', "post_detail"),
    path('update/', "post_update"),
    path('delete/', "post_delete"),
]