from django.contrib import admin
from .models import LangSession, UserDetail


class SelectedLanguageAdmin(admin.ModelAdmin):
    list_display = ('session', 'language','id')
    


# Register your models here.
admin.site.register(LangSession, SelectedLanguageAdmin)
admin.site.register(UserDetail)