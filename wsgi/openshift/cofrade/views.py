import os
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import requests,json
from cofrade import models

def home(request):
    return render_to_response('home.html')

