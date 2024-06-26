from .models import SiteConfig, Navigation
from translation.models import Translation, TranslationKey, Language
from user.models import LangSession

def site_config(request):
    siteTitle = SiteConfig.objects.get(key='titleBaseName')
    navigation_list = Navigation.objects.filter(is_active=True)
    data = {
        'siteName':siteTitle.value, # .value önemli
        'navigation_list':navigation_list
    }
    return data


def lang_translations(request):
    sessionKey = request.session.session_key
    if(not sessionKey):
        request.session.create()
        sessionKey = request.session.session_key

    try:
        user_language = LangSession.objects.get(session=sessionKey).language.id
    except LangSession.DoesNotExist:
        user_language = SiteConfig.objects.get(key='siteLanguage').value
    
    available_langs = Language.objects.filter(is_selectable=True)
    
    if not user_language in available_langs.values_list('id', flat=True):
        user_language = SiteConfig.objects.get(key='siteLanguage').value

    user_lang_no = Language.objects.get(pk=user_language).name
    translation_list = {}
    
    translationKey_list = TranslationKey.objects.all()
    for translationKey in translationKey_list:
        try:
            try:
                lang_item = Translation.objects.get(key=translationKey, language=user_language)   
            except Translation.DoesNotExist:
                lang_item = Translation.objects.get(key=translationKey, language=1)
            translation_list[translationKey.key] = lang_item.value
        except Translation.DoesNotExist:
            translation_list[translationKey.key] = translationKey.key
            
    
    data = {
        'lang':translation_list,
        'available_langs':available_langs,
        'sessionKey':sessionKey,
        'user_lang_no':user_lang_no,
    }

    return data

