
from django.urls import path
from . import views
from .views import list_clientes, create_cliente, update_cliente, delete_cliente


urlpatterns = [

    path("", views.login, name='admin'),
    path("cadastro/", views.cadastro, name='cadastro'),
    path("menu/", views.menu, name='menu'),
    path('login/', views.login,name = 'login'),
    path('cadastrarcomeia/', views.cadastrarcomeia,name='cadastrarcomeia'),
    path('addcolheita/',views.addcolheita, name='addcolheita'),

#teste
    path('lista/', list_clientes, name='list_clientes'),
    path('new/', create_cliente, name='create_clientes'),
    path('update/<int:id>/', update_cliente, name='update_cliente'),
    path('delete/<int:id>/', delete_cliente, name='delete_cliente'),
]

