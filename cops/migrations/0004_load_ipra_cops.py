# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 21:59
from __future__ import unicode_literals
from django.db import migrations
from settlements.settings import BASE_DIR
import csv
from cops.models import IPRACop
from cases.models import IPRACase


def load_ipra_cops(apps,schema_editor):
    infile_path = BASE_DIR + '/cops/migrations/ipra_officers.csv'
    infile      = open(infile_path)
    incsv       = csv.DictReader(infile)

    for row in incsv:
        # split names
        if not row['Accused']:
            continue
        last_name  = row['Accused'].split(',')[0]
        first_name = row['Accused'].split(',')[1]
        
        # lookup case
        ipra_cases  = list(IPRACase.objects.filter(cr_no=row['CR']))
        if len(ipra_cases) != 1:
            print 'ambiguous/unknown ipra case cr:', row['CR']
            break
        else:
            ipra_case = ipra_cases[0]

        try: 
            ic = IPRACop.objects.create(
                    case            = ipra_case,
                    cop_first_name  = first_name,
                    cop_last_name   = last_name,
                    badge_no        = row['Star'],
                    cr_no           = row['CR'],
                    finding         = row['Finding'],
                    discipline_code = row['Discipline_Code'],
                    discipline      = row['Discipline']
                    )
            ic.save()
        except Exception, e:
            import ipdb; ipdb.set_trace()


class Migration(migrations.Migration):

    dependencies = [
        ('cops', '0003_load_casecops'), 
    ]

    operations = [
            migrations.RunPython(load_ipra_cops)
    ]