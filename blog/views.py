from django.shortcuts import render, redirect
from settings.models import Navigation


def home(request):
    return render(request, 'blog/index.html')


