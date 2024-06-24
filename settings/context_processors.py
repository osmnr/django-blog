from .models import SiteConfig, Navigation


def site_config(request):
    siteTitle = SiteConfig.objects.get(key='titleBaseName')
    navigation_list = Navigation.objects.filter(is_active='True')
    data = {
        'siteName':siteTitle.value, # .value önemli
        'navigation_list':navigation_list
    }
    return data



    