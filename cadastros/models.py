from django.db import models

# Create your models here.
# Aqui vou criar todas as classes dos diagramas de classe
# class Planta(models.Model):
#     sigla = models.CharField(max_length=2, unique=True)
#     nome = models.CharField(max_length=50)

#     def __str__(self):
#         return self.sigla + ' - ' + self.nome

class Planta(models.Model): 
    nome_popular = models.CharField(max_length=50, verbose_name="Nome Popular")
    plantio = models.DateField(help_text="Insira a data do plantio")

    def __str__(self):
        return "{} ({})".format(self.nome_popular, self.plantio)


class Especies(models.Model):
    nome_especie = models.CharField(max_length=50, verbose_name="Nome da Espécie")

    def __str__(self):
        return "{} ".format(self.nome_especie)

class Cuidado(models.Model):
    qntd_adubacao = models.CharField(max_length=50, verbose_name="Quantidade de Adubação")
    data_adubacao = models.DateField(verbose_name="Data da Adubação ")
    data_rega = models.DateField(verbose_name="Data da Rega")

    def __str__(self):
        return "{} ({})".format( self.data_adubacao, self.data_rega)

class Perfil(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome")
    sobrenome = models.CharField(max_length=30, verbose_name="Sobrenome")
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento")
    cuidador = models.CharField(max_length=50, help_text="Explique a quanto tempo é cuidador de plantas")

    def __str__(self):
        return "{} ({})".format(self.nome, self.dt_nascimento)

class Sugestoes(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Sugestões e Melhorias")

    def __str__(self):
        return "{}".format(self.descricao)

