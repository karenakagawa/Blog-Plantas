from os import name
from django.urls import path

#importar as views que a gente criou
from .views import PlantaCreate, PlantaUpdate, PlantaDelete, PlantaList, EspeciesCreate, EspeciesUpdate, EspeciesDelete, EspeciesList, CuidadoCreate, CuidadoUpdate, CuidadoDelete, CuidadoList, PerfilCreate, PerfilUpdate, PerfilDelete, PerfilList, SugestoesCreate, SugestoesUpdate, SugestoesDelete, SugestoesList

#tem que ser urlpatterns pq é padrão do Django
urlpatterns = [
# Criar todos os endereços/rotas
    path("cadastrar/planta/", PlantaCreate.as_view(), name= "cadastrar-planta"),
    path("editar/planta/<int:pk>", PlantaUpdate.as_view(), name= "editar-planta"),
    path("excluir/planta/<int:pk>", PlantaDelete.as_view(), name= "delete-planta"),
    path("listar/planta/", PlantaList.as_view(), name= "listar-planta"),

    path("cadastrar/especies/", EspeciesCreate.as_view(), name= "cadastrar-especies"),
    path("editar/especies/<int:pk>", EspeciesUpdate.as_view() ,name= "editar-especie"),
    path("excluir/especies/<int:pk>", EspeciesDelete.as_view(),name= "excluir-especie"),
    path("listar/especies/", EspeciesList.as_view(), name= "listar-especies"),

    path("cadastrar/cuidado/", CuidadoCreate.as_view(), name= "cadastrar-cuidado"),
    path("editar/cuidado/<int:pk>", CuidadoUpdate.as_view(), name= "editar-cuidado"),
    path("excluir/cuidado/<int:pk>", CuidadoDelete.as_view(), name= "excluir-cuidado"),
    path("listar/cuidado/", CuidadoList.as_view(), name= "listar-cuidado"),

    path("cadastrar/perfil/", PerfilCreate.as_view(), name= "cadastrar-perfil"),
    path("editar/perfil/<int:pk>", PerfilUpdate.as_view(), name= "editar-perfil"),
    path("excluir/perfil/<int:pk>", PerfilDelete.as_view(), name= "excluir-perfil"),
    path("listar/perfil/", PerfilList.as_view(), name= "listar-perfil"),

    path("cadastrar/sugestoes/", SugestoesCreate.as_view(), name= "cadastrar-sugestoes"),
    path("editar/sugestoes/<int:pk>", SugestoesUpdate.as_view(), name= "editar-sugestoes"),
    path("excluir/sugestoes/<int:pk>", SugestoesDelete.as_view(), name= "excluir-sugestoes"),
    path("listar/sugestoes/", SugestoesList.as_view(), name= "listar-sugestoes")]
    