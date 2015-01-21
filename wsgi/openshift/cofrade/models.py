from django.db import models
from django.contrib import admin

# Create your models here.

class Cofradia(models.Model):
    nombre = models.CharField(max_length=200)
    nombrecorto = models.CharField(max_length=100)
    sede = models.CharField(max_length=50)
    annofundacion = models.IntegerField()
    diaprocesion = models.CharField(max_length=20)
    numhermanos = models.IntegerField()
    hermanomayor = models.CharField(max_length=25)

class Paso(models.Model):
    codigocofradia = models.ForeignKey(Cofradia)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10)
    numcostaleros = models.IntegerField()
    numnazarenos = models.IntegerField()
    colorcapa = models.CharField(max_length=10)
    colorantifaz =  models.CharField(max_length=10)

admin.site.register(Cofradia)
admin.site.register(Paso)



