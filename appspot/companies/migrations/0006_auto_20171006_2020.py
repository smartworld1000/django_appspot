# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:20
from __future__ import unicode_literals

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20171006_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=localflavor.us.models.USZipCodeField(help_text='', max_length=10),
        ),
    ]
