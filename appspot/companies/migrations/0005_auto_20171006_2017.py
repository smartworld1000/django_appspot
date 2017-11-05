# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:17
from __future__ import unicode_literals

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20171006_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=localflavor.us.models.USZipCodeField(help_text='', max_length=10),
        ),
    ]
