# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-16 16:49
from __future__ import unicode_literals
from django.db import migrations
from cops.models import IPRACop
from datetime import datetime

def tie_breaker(apps,schema_editor):
    """
    revised derivations
    to better utilize badge
    numbers to break ties
    """
    icops = IPRACop.objects.all()
    unmatched_icops = [x for x in icops if not x.cop]
    for icop in unmatched_icops:
        prob_matches = icop.qualify_matches()['probable']
        if len(prob_matches) == 1:
            icop.cop = prob_matches[0]
            icop.matched_by = 'auto'
            icop.matched_when = datetime.now()
            icop.save()
            print 'matching ipracop', icop.id
        else:
            print 'no match found for ipracop', icop.id
            


class Migration(migrations.Migration):

    dependencies = [
        ('cops', '0006_make_ipra_matches'),
    ]

    operations = [
            migrations.RunPython(tie_breaker)
    ]
