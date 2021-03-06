# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
        ('investigative_cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case_contact',
            fields=[
                ('case_contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_contacts', to='person.Person', verbose_name='Person')),
                ('investigative_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_contacts', to='investigative_cases.Investigative_case', verbose_name='Investigative case')),
            ],
            options={
                'verbose_name': 'case_contact',
                'verbose_name_plural': 'case_contacts',
            },
        ),
    ]
