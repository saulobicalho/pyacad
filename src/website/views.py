from django.views.generic import ListView
from pyacad.models import Funcionario

class ListaFuncionarios(ListView):
    template_name = "templates/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"
