# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_types', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense_type',
            old_name='expense_type_id',
            new_name='id',
        ),
    ]
