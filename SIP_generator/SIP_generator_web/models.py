from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

class MetaData(models.Model):
	
	contributor = models.CharField(max_length=255)
	coverage = models.CharField(max_length=255)
	'''creator = models.CharField(max_length=255)
	date = models.DateField()
	descripition = models.CharField(max_length=255)
	formats = models.CharField(max_length=255)
	identifier = models.CharField(max_length=255)
	language = models.CharField(max_length=255)
	publisher = models.CharField(max_length=255)
	relation = models.CharField(max_length=255)
	rights = models.CharField(max_length=255)
	source = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	types = models.CharField(max_length=255)'''


	class Meta:
		db_table = 'MetaDatas'
		verbose_name = 'MetaData'
		verbose_name_plural = 'MetaDatas'