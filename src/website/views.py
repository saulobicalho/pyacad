from django.shortcuts import render

# Create your views here.
def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objetos.all()

    # Incluímos no contexto
    contexto = {
      'funcionarios': funcionarios
    }

    # Retornamos o template no qual os funcionários serão dispostos
    return render(request, "funcionarios.html", contexto)
