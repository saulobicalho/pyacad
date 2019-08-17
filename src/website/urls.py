# Importamos a função index() definida no arquivo views.py
from website import views
from django.urls import path
from website.views import IndexTemplateView

app_name = 'website'


# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    path('', IndexTemplateView.as_view()),
]
