# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20171005_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='plate_expiration',
            field=models.DateField(help_text=''),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='record_creation_date',
            field=models.DateField(help_text=''),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registered_address',
            field=localflavor.us.models.USZipCodeField(help_text='', max_length=10),
        ),
    ]
