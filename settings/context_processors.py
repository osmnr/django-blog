from .models import SiteConfig, Navigation
from translation.models import Translation, TranslationKey, Language


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
    
    translation_list = {}
    default_lang = SiteConfig.objects.get(key='siteLanguage').value
    available_langs = Language.objects.filter(is_selectable=True)
    translationKey_list = TranslationKey.objects.all()
    
    for translationKey in translationKey_list:

        try:
            lang_item = Translation.objects.get(key=translationKey, language=2) # session'dan seçtiğimizi buraya koyucaz
        except Translation.DoesNotExist:
            lang_item = Translation.objects.get(key=translationKey, language=default_lang)
        
        translation_list[translationKey.key] = lang_item.value
    

    data = {
        'lang':translation_list,
        'available_langs':available_langs,
        'sessionKey':sessionKey
    }

    return data

