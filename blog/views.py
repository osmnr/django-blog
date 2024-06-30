from django.shortcuts import render, redirect
from settings.models import Navigation


def home(request):
    return render(request, 'blog/index.html')



def detail(request):
    return render(request, 'blog/detail.html')


def archive(request):
    return render(request, 'blog/archive.html')


