from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
import csv

from .forms import *


# Create your views here.

def index(request):
	return render(request, 'SIP_generator_web/index.html', locals())

def cadastro(request):
	return render(request, 'SIP_generator_web/cadastro.html', locals())

def login(request):
	return render(request, 'SIP_generator_web/login.html', locals())


def newSIP(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=test.csv'
	form = DublinCoreMeta(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			contributor = form.cleaned_data['contributor']
			coverage = form.cleaned_data['coverage']

			writer = csv.writer(response)
			writer.writerow([contributor, ",", coverage])

	return render(request, 'SIP_generator_web/newSIP.html', {'form': form})