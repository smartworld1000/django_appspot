# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_expenses', '0003_auto_20171005_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_expense',
            name='expense_date',
            field=models.DateField(help_text=''),
        ),
    ]
