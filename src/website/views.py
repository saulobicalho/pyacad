from django.http import HttpResponse
from django.shortcuts import render
from pyacad.models import Funcionario

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objetos.all()

    # Incluímos no contexto
    contexto = {
      'funcionarios': funcionarios
    }

    # Retornamos o template no qual os funcionários serão dispostos
    return render(request, "templates/funcionarios.html", contexto)


""" python manage.py runserver"""
