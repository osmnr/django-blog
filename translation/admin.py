from django.contrib import admin
from .models import Language, Translation, TranslationKey



class LanguageAdmin(admin.ModelAdmin):
    #search_fields = ('name','is_selectable')
    list_display = ('name', 'is_selectable')
    list_filter = ('name', 'is_selectable')
    #ordering = ('name', 'is_selectable')


# Register your models here.
admin.site.register(Language,LanguageAdmin)
admin.site.register(Translation)
admin.site.register(TranslationKey)
