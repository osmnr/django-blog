from django.shortcuts import render, redirect
from translation.models import Language
from .models import LangSession
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def userRegister(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    if request.method == 'POST':
        inputUserName = request.POST.get('formUserName')
        inputPassword = request.POST.get('formPassword')
        inputPassword2 = request.POST.get('formPassword2')
        inputEmail = request.POST.get('formEmail')
        if inputPassword == inputPassword2:
            try:
                user = User.objects.create_user(username=inputUserName, password=inputPassword, email=inputEmail)
                user.save()
                login(request,user)
                return redirect('blog:home')
            except Exception as e:
                messages.error(request,f'error:{str(e)}')
        else:
            messages.error(request, 'Passwords do not match..')
    return render(request,'user/register.html')




def userLogout(request):
    if not request.user.is_authenticated:
        return redirect('blog:home')
    logout(request)
    return redirect('user:userLogin')



def userLogin(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    if request.method == 'POST':
        inputUserName = request.POST.get('formUserName')
        inputPassword = request.POST.get('formPassword')
        user = authenticate(request,username=inputUserName, password=inputPassword)
        if user is not None:
            login(request,user)
            return redirect('blog:home')
        else:
            messages.error(request, 'Username or password is not correct...')
    return render(request,'user/login.html')


def selected_language(request):
    previous_page = request.META.get('HTTP_REFERER')
    if not previous_page:
        previous_page = "blog:test"
    
    session_key = request.session.session_key

    if request.method == 'POST':
        selected_language_id = int(request.POST.get('language'))
        if selected_language_id:        
            try:
                language_instance = Language.objects.get(pk=selected_language_id, is_selectable=True)
                try:
                    language_selected = LangSession.objects.get(session=session_key)
                    language_selected.language = language_instance
                    language_selected.save()
                
                except LangSession.DoesNotExist:
                    language_selected = LangSession.objects.create(session=session_key,language=language_instance )

            except Language.DoesNotExist:
                pass

    return redirect(previous_page)



def userProfileInfo(request):
    return render(request,'user/userProfileDetail.html')