from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required

from .forms import *


# Create your views here.

def index(request):
	return render(request, 'SIP_generator_web/index.html', locals())

def cadastro(request):
	return render(request, 'SIP_generator_web/cadastro.html', locals())

def login(request):
	return render(request, 'SIP_generator_web/login.html', locals())