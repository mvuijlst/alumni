# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0024_auto_20150720_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(choices=[('overlijden', 'Overlijden'), ('overige', 'Overige'), ('geboorte', 'Geboorte'), ('huwelijk', 'Huwelijk')], max_length=10, default='geboorte'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('website', 'Website'), ('twitter', 'Twitter'), ('telefoon', 'Telefoon'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn')], max_length=10, default='gsm'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('A', 'ander'), ('V', 'vrouw'), ('M', 'man'), ('?', 'onbekend')], max_length=1, default='M'),
        ),
    ]
