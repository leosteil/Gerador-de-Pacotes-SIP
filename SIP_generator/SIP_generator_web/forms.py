from django import forms
from django.contrib import admin
from django.conf import settings
from .models import *

class DublinCoreMeta(forms.Form):
	contributor = forms.CharField(label="Contributor", max_length=255, required = False)
	coverage = forms.CharField(label="Covarage", max_length=255, required = False)
	"""creator = forms.CharField(label="Creator", max_length=255)
	date = forms.DateField(label="Date")
	descripition = forms.CharField(label="Descripiton", max_length=255)
	format_ = forms.CharField(label="Format", max_length=255)
	identifier = forms.CharField(label="Identifier", max_length=255)
	language = forms.CharField(label="Language", max_length=255)
	publisher = forms.CharField(label="Publisher", max_length=255)
	relation = forms.CharField(label="Relation", max_length=255)
	rights = forms.CharField(label="Rights", max_length=255)
	source = forms.CharField(label="Source", max_length=255)
	subject = forms.CharField(label="Subject", max_length=255)
	title = forms.CharField(label="Title", max_length=255)
	type_ = forms.CharField(label="Type", max_length=255)"""



