from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('setlanguage', views.selected_language, name="setlanguage")
]
