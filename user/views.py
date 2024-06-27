from django.shortcuts import render, redirect
from translation.models import Language
from .models import LangSession


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