from django.shortcuts import render,redirect
from translation.models import Language
from .models import LangSession

def selected_language(request):
    previous_page = request.META.get('HTTP_REFERER')
    session_key = request.session.session_key

    if request.method == 'POST':
        selected_language_id = int(request.POST.get('language'))
        if selected_language_id:        
            try:
                language_instance = Language.objects.get(pk=selected_language_id, is_selectable=True)
                session_language, created = LangSession.objects.get_or_create(session=session_key)
                session_language.language = language_instance
                session_language.save()

            except Language.DoesNotExist:
                pass

    return redirect(previous_page)