# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 15:57
from __future__ import unicode_literals
from django.db import migrations
from cases.models import IPRACase
from settlements.settings import BASE_DIR
import csv
from utils.types import parse_str_date


def load_ipra_cases(apps,schema_editor):
    infile_path = BASE_DIR + '/cases/migrations/ipra_cases.csv'
    infile      = open(infile_path)
    incsv       = csv.DictReader(infile)

    for row in incsv:

        ic = IPRACase.objects.create(
                cr_no          = row['CR'],
                incident_date  = parse_str_date(row['Incident_DateTime']),
                complaint_date = parse_str_date(row['Complaint_Date']),
                category_code  = row['Category_Code'],
                description    = row['Description'],
                )
        ic.save()



class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_load_civil_cases'),
    ]

    operations = [
            migrations.RunPython(load_ipra_cases)
    ]
