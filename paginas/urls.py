from os import name
from django.urls import path

from.views import PaginaInicial
from.views import Sobre


urlpatterns = [
# Criar todos os endereços/rotas
#path('endereco/', MinhaView.as_view(), name='referencias/apelido'),
path('inicio/', PaginaInicial.as_view(), name='index'),
path('sobre/', Sobre.as_view(), name='sobre'),


]