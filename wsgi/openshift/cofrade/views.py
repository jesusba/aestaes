from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
import requests,json
from cofrade import models
from django.contrib.auth.models import User
from cofrade.functions import *

def home(request):
    return render_to_response('home.html')

