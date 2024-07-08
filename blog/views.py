from django.shortcuts import render, redirect, get_object_or_404
from settings.models import Navigation
from .models import BlogPost, Category
from django.contrib.auth.decorators import login_required
from user.models import UserDetail
from django.contrib import messages


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
    if request.method =='POST':
        myAuthor = request.user
        inputTitle = request.POST.get('inputTitle')
        inputCategory = request.POST.get('inputCategory')
        inputCategory = Category.objects.get(id=inputCategory)
        inputContent = request.POST.get('inputContent')
        inputImage = request.FILES.get('inputImage')
        try:
            a = BlogPost.objects.create(title=inputTitle,author=myAuthor, image=inputImage,content=inputContent, category=inputCategory)
            a.save()
            return redirect('blog:home')
        except BlogPost.DoesNotExist:
            messages.error(request, 'Inavalid entry')
    data = {
        'categories':category_list,
    }
    return render(request, 'blog/addpost.html',data)


def detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    user = UserDetail.objects.get(username=post.author.id)
    data = {
        'post':post,
        'user':user,
    }
    return render(request, 'blog/detail.html', data)



def archive(request):
    post_list = BlogPost.objects.all()
    category_list = Category.objects.all()
    data = {
        'postList': post_list,
        'categories':category_list,
    }
    return render(request, 'blog/archive.html', data)


