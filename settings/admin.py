from django.contrib import admin
from .models import SiteConfig, Navigation

class SiteConfigAdmin(admin.ModelAdmin):
    search_fields = ('key', 'value')
    list_display = ('key', 'value')
    list_filter = ('key', 'value')
    ordering = ('key', 'value')
    
admin.site.register(SiteConfig,SiteConfigAdmin)
admin.site.register(Navigation)
