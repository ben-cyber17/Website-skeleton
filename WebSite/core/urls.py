# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prodotti/', views.lista_prodotti, name='prodotti'),
    path('tecnologie/', views.lista_tecnologie, name='tecnologie'),
    path('lavora-con-noi/', views.lavora_con_noi, name='lavora_con_noi'),
    path('contatti/', views.contatti, name='contatti'),
]
