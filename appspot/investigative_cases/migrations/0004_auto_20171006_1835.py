# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigative_cases', '0003_auto_20171005_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigative_case',
            name='file_received_date',
            field=models.DateField(help_text=''),
        ),
        migrations.AlterField(
            model_name='investigative_case',
            name='injury_date',
            field=models.DateField(help_text=''),
        ),
        migrations.AlterField(
            model_name='investigative_case',
            name='is_active',
            field=models.BooleanField(help_text=''),
        ),
        migrations.AlterField(
            model_name='investigative_case',
            name='record_creation_date',
            field=models.DateField(auto_now_add=True, help_text=''),
        ),
    ]
