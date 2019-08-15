# Importamos a função index() definida no arquivo views.py
from . import views
from django.urls import path, re_path

app_name = 'website'

# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    # GET /
    """path('', views.index),
    path('funcionarios/<int:ano>/', views.funcionarios_por_ano)"""
    path('lista/', views.lista_funcionarios)
]
