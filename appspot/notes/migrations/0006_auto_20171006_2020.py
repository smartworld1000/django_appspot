# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20171006_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_time',
            field=models.DateTimeField(help_text=''),
        ),
        migrations.AlterField(
            model_name='note',
            name='record_creation_date',
            field=models.DateField(help_text=''),
        ),
    ]