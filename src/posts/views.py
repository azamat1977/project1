
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    return HttpResponse("<h1>Deateil</h1>")

def posts_list(request):
    return HttpResponse("<h1>List</h1>")

def posts_update(request):
    return HttpResponse("<h1>Update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>Delete</h1>")