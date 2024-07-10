from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('setlanguage', views.selected_language, name="setlanguage"),
    path('login/', views.userLogin, name='userLogin'),
    path('logout/',views.userLogout, name='userLogout'),
    path('register/',views.userRegister, name='userRegister'),
    path('profile/', views.userProfileInfo, name='userProfileInfo'),
]
