from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('us/', views.contactUs, name='contactUs'),
]
