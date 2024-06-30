from django.shortcuts import render


def contactUs(request):
    return render(request, 'contact/contact.html')

