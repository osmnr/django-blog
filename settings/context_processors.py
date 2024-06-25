from .models import SiteConfig, Navigation
from translation.models import Translation, TranslationKey

def site_config(request):
    siteTitle = SiteConfig.objects.get(key='titleBaseName')
    navigation_list = Navigation.objects.filter(is_active='True')
    data = {
        'siteName':siteTitle.value, # .value önemli
        'navigation_list':navigation_list
    }
    return data


def lang_translations(request):
    
    translationKey_list = TranslationKey.objects.all()
    translation_list = dict()
    default_lang = SiteConfig.objects.get(key='siteLanguage')


    for key in translationKey_list:
        try:
            lang_item = Translation.objects.filter(key=key, language=2)
        except:
            lang_item = Translation.objects.filter(key=key, language=int(default_lang))
        translation_list[key.key] = key.value

    data = {
        'translation_list':translation_list
    }

    return data

