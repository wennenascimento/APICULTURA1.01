from django.urls import path
#from .views import start
#from .views import cadastro
from .import views

urlpatterns = [
    path('start/', views.start, name= 'start'),
    path('cadastro/', views.cadastro, name='cadastro'),
]