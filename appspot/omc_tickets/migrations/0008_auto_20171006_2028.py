# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omc_tickets', '0007_auto_20171006_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omc_ticket',
            name='date_closed',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='omc_ticket',
            name='date_opened',
            field=models.DateTimeField(help_text=''),
        ),
    ]