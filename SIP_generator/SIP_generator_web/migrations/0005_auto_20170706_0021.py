# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-06 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIP_generator_web', '0004_auto_20170705_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='accessConditions',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='creationDates',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='creationDatesEnd',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='creationDatesStart',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='creationDatesType',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='creators',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='extendAndMedium',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='language',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='locationOfOriginals',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='placeAccessPoints',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='scopeAndContent',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='subjectAccessPoint',
            field=models.CharField(max_length=255, null=True),
        ),
    ]