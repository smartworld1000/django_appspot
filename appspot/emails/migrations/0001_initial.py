# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_type', models.CharField(choices=[('HOME', 'Home'), ('WORK', 'Work'), ('OTHER', 'Other')], max_length=100, verbose_name='Email type')),
                ('email_address', models.EmailField(help_text='', max_length=254)),
                ('email_label', models.CharField(max_length=100, verbose_name='Email label')),
                ('record_owner', models.CharField(max_length=100, verbose_name='Record owner')),
                ('record_creation_date', models.DateField(help_text='')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_addresses', to='person.Person', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'email',
                'verbose_name_plural': 'emails',
            },
        ),
    ]