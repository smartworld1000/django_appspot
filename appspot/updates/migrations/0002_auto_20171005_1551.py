# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='activity_date',
            field=models.DateField(help_text=''),
        ),
    ]
