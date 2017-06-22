from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
import csv, sys
import MySQLdb as dbapi
from glob import glob; from os.path import expanduser
from django.db import connection, transaction

from .forms import *


# Create your views here.

def index(request):
	return render(request, 'SIP_generator_web/index.html', locals())

def cadastro(request):
	return render(request, 'SIP_generator_web/cadastro.html', locals())

def login(request):
	return render(request, 'SIP_generator_web/login.html', locals())


def newSip(request):
    if request.method == 'POST':
        form = DublinCoreMeta(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            return render(request, 'SIP_generator_web/newSIP.html')
    else:
        form = DublinCoreMeta()

    context = {
        'form': form
    }
    return render(request, 'SIP_generator_web/newSIP.html', context)

def empacotar(request):
    cursor = connection.cursor()
    #cursor.execute("select * from MetaDatas")

    cursor.execute("SELECT * FROM MetaDatas INTO OUTFILE '/var/lib/mysql-files/teste.csv' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';")

    return render(request, 'SIP_generator_web/index.html', locals())