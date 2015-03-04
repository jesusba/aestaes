import os
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import requests,json
from cofrade import models

def home(request):
    return render_to_response('home.html')

def nombrecofra(request):
    cofradia = models.Cofradia.objects.all()
    return render_to_response('cofradias.html',{'data_raw': cofradia})

def nombrepaso(request):
	cofradia = models.Cofradia.objects.all()
	paso = models.Paso.objects.all().query
	query.group_by = ['diaprocesion']
    return render_to_response('pasos.html',{'data_raw': nombrecofra , 'nombre': nombre, 'dia': diaprocesion})