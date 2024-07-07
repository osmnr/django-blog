from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('detail/<slug:slug>',views.detail,name='detail'),
    path('archive/',views.archive,name='archive'),
    path('addpost/',views.addpost, name='addpost'),
]
