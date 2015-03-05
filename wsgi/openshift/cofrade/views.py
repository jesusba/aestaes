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