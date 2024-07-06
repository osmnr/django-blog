from django.shortcuts import render, redirect
from settings.models import Navigation
from .models import BlogPost, Category
from django.contrib.auth.decorators import login_required

def home(request):
    post_list = BlogPost.objects.all()
    category_list = Category.objects.all()
    data = {
        'postList': post_list,
        'categories':category_list,
    }
    return render(request, 'blog/index.html', data)

#@login_required(login_url='/user/login/') eğer settings.py'De tanımlanmadıysa, biz tanımladık
@login_required
def addpost(request):
    category_list = Category.objects.all()
    data = {
        'categories':category_list,
    }
    return render(request, 'blog/addpost.html',data)


def detail(request):
    return render(request, 'blog/detail.html')



def archive(request):
    post_list = BlogPost.objects.all()
    category_list = Category.objects.all()
    data = {
        'postList': post_list,
        'categories':category_list,
    }
    return render(request, 'blog/archive.html', data)


