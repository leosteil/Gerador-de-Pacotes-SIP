from django import forms
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
import datetime

class DublinCoreMeta(forms.ModelForm):
	filename = forms.FileField(label="Filename",max_length=255, required=True)
	title = forms.CharField(label="Title",max_length=255,required=False)
	issued = forms.DateField(label="Issued",initial=datetime.date.today)
	publisher = forms.CharField(label="Publisher",max_length=255,required=False)
	contributor = forms.CharField(label="Contributor",max_length=255,required=False)
	subject = forms.CharField(label="Subject",max_length=255,required=False)
	data = forms.DateField(label='Data',initial=datetime.date.today)
	description = forms.CharField(label="Description",max_length=255,required=False)
	notes = forms.CharField(label="Notes",max_length=255,required=False)
	isPartOf = forms.CharField(label="Is part Of",max_length=255,required=False)	
	repository = forms.CharField(label = 'Repository',max_length=255,required=False)
	rights = forms.CharField(label="Rights",max_length=255,required=False)	
	project_website = forms.CharField(label="Project web-site",max_length=255,required=False)
	_format = forms.CharField(label="Format",max_length=255,required=False)
						

	class Meta:
		model = MetaData
		#fields = ['title', 'creator', 'subject', 'publisher', 'contributor', 'date', 'tipo', 'formato', 'identifier', 'source', 'language', 'relation', 'coverage', 'rights', 'description']
		fields = ['filename', 'title', 'issued', 'publisher', 'contributor', 'subject', 'data', 'description', 'notes', 'isPartOf', 'repository', 'rights', 'project_website', '_format']