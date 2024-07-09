from django.contrib import admin
from .models import LangSession, UserDetail, Log


class SelectedLanguageAdmin(admin.ModelAdmin):
    list_display = ('session', 'language','id')



# Register your models here.
admin.site.register(LangSession, SelectedLanguageAdmin)
admin.site.register(UserDetail)
admin.site.register(Log)