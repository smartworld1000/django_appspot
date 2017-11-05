# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20171006_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_id',
            new_name='id',
        ),
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