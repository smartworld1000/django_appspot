# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0007_auto_20171006_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email_address',
            field=models.EmailField(help_text='', max_length=254),
        ),
        migrations.AlterField(
            model_name='email',
            name='record_creation_date',
            field=models.DateField(help_text=''),
        ),
    ]
