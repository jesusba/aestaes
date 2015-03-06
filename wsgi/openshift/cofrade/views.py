import os
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import requests,json
from cofrade.models import Cofradia,Paso


def home(request):
    return render_to_response('home.html')

def nombrecofra(request):
    cofradia = Cofradia.objects.all()
    return render_to_response('cofradias.html',{'data_raw': cofradia})

def nombrepaso(request):
    paso = Paso.objects.all()
    return render_to_response('pasos.html',{'data_raw': paso})

def contacto(request):
    return render_to_response('contacto.html')

def cofradetalle(request,cofradia_id):
	infocofra = Cofradia.objects.get(id=cofradia_id)
	return render_to_response('infocof.html', {"data_raw":infocofra},)

def pasodetalle(request,paso_id):
	infopaso = Paso.objects.get(id=paso_id)
	return render_to_response('infopaso.html', {"data_raw":infopaso},)