# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 22:37
from __future__ import unicode_literals
from django.db import migrations
from settlements.settings import BASE_DIR
import unicodecsv as csv
from cases.models import Case
from cops.models import Cop, CaseCop
from utils.types import parse_str_date


def destroy_all_casecops(apps,schema_editor):
    """
    because idempotency
    """
    for cc in CaseCop.objects.all():
        cc.delete()


def load_new_casecops(apps,schema_editor):
    infile_path = BASE_DIR + '/data/20160614_migration/casecops.csv'
    infile      = open(infile_path)
    incsv       = csv.DictReader(infile)

    for row in incsv:
        case_lookup = list(Case.objects.filter(case_no=row['case_no']))
        if len(case_lookup) != 1:
            print 'ambiguous case:', row['case_no'], 'has len:', len(case_lookup)
            import ipdb; ipdb.set_trace()
        else:
            # can only create casecop if we verify there's 1 matching case in cases table
            case = case_lookup[0]
            cc = CaseCop.objects.create(
                                   id   = row['id'],
                                   case = case,
                                   case_no = row['case_no'],
                                   slug = '',
                                   
                                   cop = Cop.objects.get(id=row['cop_id']) if row['cop_id'] else None,
                                   cop_first_name = row['cop_first_name'],
                                   cop_middle_initial = row['cop_middle_initial'],
                                   cop_last_name = row['cop_last_name'],
                                   badge_no = row['badge_no'],
                                   officer_atty = row['officer_atty'],
                                   officer_atty_firm = row['officer_atty_firm'],

                                   entered_by = row['entered_by'],
                                   entered_when = parse_str_date(row['entered_when']),
                                   fact_checked_by = row['fact_checked_by'],
                                   fact_checked_when = parse_str_date(row['fact_checked_when']),
                                   matched_by = row['matched_by'],
                                   matched_when = parse_str_date(row['matched_when']),
                                   note = row['note'],
                                   flag = row['flag'] == '1'
                                  )
            cc.save()



class Migration(migrations.Migration):

    dependencies = [
            ('cops','0011_load_cops_with_notes')
    ]

    operations = [
            migrations.RunPython(destroy_all_casecops),
            migrations.RunPython(load_new_casecops),
    ]
