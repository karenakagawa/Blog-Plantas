from django.contrib import admin

from .models import Planta, Especies,Cuidado, Perfil, Sugestoes 
# Register your models here.

admin.site.register(Planta)
admin.site.register(Especies)
admin.site.register(Cuidado)
admin.site.register(Perfil)
admin.site.register(Sugestoes)
