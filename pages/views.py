from django.shortcuts import render, redirect
from django.http import HttpResponse
from members.models import Photos
from pages_content.models import *
# Create your views here.


def explore(request):
    return render(request, 'explore.html', {})


def culture(request):
    c = Category.objects.get(Category='Culture')
    p = Post.objects.filter(Category=c)
    return render(request, 'culture.html', {'posts': p})


def natural(request):
    c = Category.objects.get(Category='Nature')
    p = Post.objects.filter(Category=c)
    return render(request, 'natural.html', {'posts': p})


def sport(request):
    c = Category.objects.get(Category='Sport')
    p = Post.objects.filter(Category=c)
    return render(request, 'sport.html', {'posts': p})


def gallary(request):
    queryset = Photos.objects.all()
    return render(request, 'gallary.html', {"querydata": queryset})
