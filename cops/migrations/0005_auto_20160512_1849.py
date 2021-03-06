# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cops', '0004_load_ipra_cops'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipracop',
            name='flag',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ipracop',
            name='matched_by',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipracop',
            name='matched_when',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ipracop',
            name='note',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
