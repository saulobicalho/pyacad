from django.http import HttpResponse
from django.shortcuts import render
from pyacad.models import Funcionario
from django.views.generic.base import TemplateView

class IndexTemplateView(TemplateView):
  template_name = "index.html"


"""python manage.py runserver"""
