# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
import MySQLdb as dbapi
from glob import glob; from os.path import expanduser
from django.db import connection, transaction

from .forms import *
import shutil, os, csv, sys
from os.path import expanduser


# Create your views here.

def index(request):
    return render(request, 'SIP_generator_web/index.html', locals())

def cadastro(request):
    return render(request, 'SIP_generator_web/cadastro.html', locals())

def login(request):
    return render(request, 'SIP_generator_web/login.html', locals())


def newSip(request):
    if request.method == 'POST':
        form = DublinCoreMeta(request.POST, request.FILES)
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

    cursor.execute("SELECT filename,title,issued,publisher,contributor,subject,data,description,notes,isPartOf,repository,rights,project_website,_format FROM MetaDatas INTO OUTFILE '/var/lib/mysql-files/metadata.csv' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';")
 
    home = expanduser("~")

    if not os.path.exists(home+'/Documents/CSVMetadata/'):
        os.makedirs('/home/lsteil/Documents/CSVMetadata/')


    if not os.path.exists(home+'/Documents/CSVMetadata/metadata/'):
        os.makedirs('/home/lsteil/Documents/CSVMetadata/metadata/')

    shutil.copy2('/var/lib/mysql-files/metadata.csv', home+'/Documents/CSVMetadata/metadata/')

    with open(home+'/Documents/CSVMetadata/metadata/metadata.csv', 'r') as original: data = original.read()
    with open(home+'/Documents/CSVMetadata/metadata/metadata.csv', 'w') as modified: modified.write("filename,title,dcterms.issued,dc.publisher,dc.contributor,dc.subject,dc.date,dc.description,notes,dcterms.isPartOf,repository,dc.rights,project_website,dc.format\n" + data)

    #remove o arquivo para poder usar novamente o espaço
    os.remove('/var/lib/mysql-files/metadata.csv') 

    cursor.execute('Delete from MetaDatas')

    return render(request, 'SIP_generator_web/index.html', locals())