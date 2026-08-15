from django.shortcuts import render
from members.models import Photos
from pages_content.models import Category, Post
# Create your views here.


def explore(request):
    return render(request, 'explore.html', {})


def culture(request):
    c = Category.objects.filter(Category='Culture').first()
    p = Post.objects.filter(Category=c).select_related('Category') if c else Post.objects.none()
    return render(request, 'culture.html', {'posts': p})


def natural(request):
    c = Category.objects.filter(Category='Nature').first()
    p = Post.objects.filter(Category=c).select_related('Category') if c else Post.objects.none()
    return render(request, 'natural.html', {'posts': p})


def sport(request):
    c = Category.objects.filter(Category='Sport').first()
    p = Post.objects.filter(Category=c).select_related('Category') if c else Post.objects.none()
    return render(request, 'sport.html', {'posts': p})


def gallary(request):
    queryset = Photos.objects.all().select_related('user')
    return render(request, 'gallary.html', {"querydata": queryset})

