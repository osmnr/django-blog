from .models import SiteConfig

def site_config(request):
    siteTitle = SiteConfig.objects.get(key='titleBaseName')
    data = {
        'siteName':siteTitle.value # .value önemli
    }
    return data



    