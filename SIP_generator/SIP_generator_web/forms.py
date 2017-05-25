from django import forms
from django.contrib import admin
from django.conf import settings
from .models import *

class DublinCoreMeta(forms.ModelForm):
	contributor = forms.CharField(label="Contributor", max_length=255)
	coverage = forms.CharField(label="Covarage", max_length=255)
	creator = forms.CharField(label="Creator", max_length=255)
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
	type_ = forms.CharField(label="Type", max_length=255)

	""""class Meta:
		model = User
		fields = ['nome', 'email', 'password1', 'password2', 'telefone', 'rua', 'cep', 'bairro', 'cpf']

	def clean(self):
		cleaned_data = super(CadastroUFForm, self).clean()
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
		return self.cleaned_data

	def save(self, commit=True):
		user = super(CadastroUFForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


	def __init__(self, *args, **kwargs):
		super(CadastroUFForm, self).__init__(*args, **kwargs)
		self.fields['nome'].widget.attrs['class']="form-control"
		self.fields['email'].widget.attrs['class']="form-control"
		self.fields['password1'].widget.attrs['class']="form-control"
		self.fields['password2'].widget.attrs['class']="form-control"

		self.fields['telefone'].widget.attrs['class']="form-control"
		self.fields['rua'].widget.attrs['class']="form-control"
		self.fields['cep'].widget.attrs['class']="form-control"
		self.fields['bairro'].widget.attrs['class']="form-control"
		self.fields['cpf'].widget.attrs['class']="form-control"""
		