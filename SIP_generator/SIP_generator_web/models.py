# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from os.path import expanduser
home = home = expanduser("~")


class MetaData(models.Model):

	filename = models.FileField(max_length=255,upload_to=home+'/Documents/CSVMetadata/')
	title = models.CharField(max_length=255)
	issued = models.DateField()
	publisher = models.CharField(max_length=255)
	contributor = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	date = models.DateField()
	description = models.CharField(max_length=255)
	notes = models.CharField(max_length=255)
	isPartOf = models.CharField(max_length=255)	
	repository = models.CharField(max_length=255)
	rights = models.CharField(max_length=255)	
	project_website = models.CharField(max_length=255)
	_format = models.CharField(max_length=255)

	class Meta:
		db_table = 'MetaDatas'
		verbose_name = 'MetaData'
		verbose_name_plural = 'MetaDatas'