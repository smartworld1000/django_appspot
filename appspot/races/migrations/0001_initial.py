# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('race_id', models.AutoField(primary_key=True, serialize=False)),
                ('race', models.CharField(max_length=100, verbose_name='Race')),
            ],
        ),
    ]
