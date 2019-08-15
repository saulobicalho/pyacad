# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'

# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    # GET /
    url(r'^$', views.index, name='index'),
    path('funcionarios/<int:ano>/', views.funcionarios_por_ano)
]
