# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Cofradia(models.Model):
    nombre = models.CharField(max_length=300)
    nombrecorto = models.CharField(max_length=100)
    sede = models.CharField(max_length=50)
    annofundacion = models.IntegerField()
    numhermanos = models.IntegerField()
    hermanomayor = models.CharField(max_length=25)
    diaprocesion = models.CharField(max_length=20)
    hora = models.DateTimeField()
    def __unicode__(self):
        return self.nombrecorto

class Paso(models.Model):
    cofradia = models.ForeignKey(Cofradia)
    nombre = models.CharField(max_length=50)
    numcostaleros = models.IntegerField()
    numnazarenos = models.IntegerField()
    numpasos = models.IntegerField()
    colorcapa = models.CharField(max_length=10)
    colorantifaz =  models.CharField(max_length=10)
    def __unicode__(self):
        return "%s, %s" % (self.cofradia,self.nombre)

