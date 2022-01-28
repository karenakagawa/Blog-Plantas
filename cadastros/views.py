from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


from. models import Planta, Especies, Cuidado, Perfil, Sugestoes

from django.urls import reverse_lazy
#Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin

class PlantaCreate(CreateView):
    model = Planta
    fields = ["nome_popular", "plantio"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

class PlantaUpdate(UpdateView):
    model = Planta
    fields = ["nome_popular", "plantio"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

class EspeciesCreate(CreateView):
    model = Especies
    fields = ["nome_especie"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

class EspeciesUpdate(UpdateView):
    model = Especies
    fields = ["nome_especie"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class CuidadoCreate(CreateView):
    model = Cuidado
    fields = ["data_adubacao", "data_rega"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

class CuidadoUpdate(UpdateView):
    model = Cuidado
    fields = ["data_adubacao", "data_rega"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

class PerfilCreate(CreateView):
    model = Perfil
    fields = ["nome", "sobrenome", "dt_nascimento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ["nome", "sobrenome", "dt_nascimento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

class SugestoesCreate(CreateView):
    model = Sugestoes
    fields = ["descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

class SugestoesUpdate(UpdateView):
    model = Sugestoes
    fields = ["descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

#####Delete

class PlantaDelete(DeleteView):
    model = Planta
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")

class EspeciesDelete(DeleteView):
    model = Especies
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")

class CuidadoDelete(DeleteView):
    model = Cuidado
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")

class PerfilDelete(DeleteView):
    model = Perfil
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")

class SugestoesDelete(DeleteView):
    model = Sugestoes
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("index")

##############List

class PlantaList(ListView):
    model = Planta
    template_name = "cadastros/listas/planta.html"
    success_url = reverse_lazy("index")

class EspeciesList(ListView):
    model = Especies
    template_name = "cadastros/listas/especies.html"
    success_url = reverse_lazy("index")

class CuidadoList(ListView):
    model = Cuidado
    template_name = "cadastros/listas/cuidado.html"
    success_url = reverse_lazy("index")

class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = "cadastros/listas/perfil.html"
    success_url = reverse_lazy("index")

class SugestoesList(ListView):
    login_url = reverse_lazy('login')
    model = Sugestoes
    template_name = "cadastros/listas/sugestoes.html"
    success_url = reverse_lazy("index")

