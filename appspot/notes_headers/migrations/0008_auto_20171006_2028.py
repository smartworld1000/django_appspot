# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_headers', '0007_auto_20171006_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes_header',
            name='date_worked',
            field=models.DateField(help_text=''),
        ),
        migrations.AlterField(
            model_name='notes_header',
            name='notes_complete',
            field=models.BooleanField(help_text=''),
        ),
        migrations.AlterField(
            model_name='notes_header',
            name='wunderground_temp',
            field=models.FloatField(help_text=''),
        ),
    ]
