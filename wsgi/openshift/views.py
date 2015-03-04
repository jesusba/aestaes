import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html')

def nombrecofra(request):
    cofradia = models.Cofradia.objects.all()
    return render_to_response('cofradias.html',{'data_raw': cofradia})

def nombrepaso(request):
	dia = models.Paso.objects.all()
    return render_to_response('pasos.html', {'data_raw': dia})
