from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('detail/',views.detail,name='detail'),
    path('archive/',views.archive,name='archive'),
]
