from django.shortcuts import render, redirect
from settings.models import Navigation


# Create your views here.
def test(request):
    return render(request, 'test.html')


def test2(request):
    a = Navigation.objects.get(name='Home2')
    if (a.is_active == False):
        return redirect('blog:test')
    else:
        return render(request, 'test2.html')