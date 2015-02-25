import os
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import requests,json
from cofrade import models
from cofrade.functions import *

def home(request):
    return render_to_response('home.html')

