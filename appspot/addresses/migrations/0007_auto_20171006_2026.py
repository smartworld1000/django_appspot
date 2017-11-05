# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0006_auto_20171006_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='location_address',
            field=localflavor.us.models.USZipCodeField(help_text='', max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='record_creation_date',
            field=models.DateField(help_text=''),
        ),
    ]
