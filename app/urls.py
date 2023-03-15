
from django.urls import path
from . import views

urlpatterns = [

    path("", views.login, name='login'),
    path("cadastro/", views.cadastro, name='cadastro'),
    path("menu/", views.menu, name='menu'),
    path ('login/', views.login,name = 'login'),
    path('cadastrarcomeia/', views.cadastrarcomeia,name='cadastrarcomeia'),
    path('header/',views.header, name='header'),

]

