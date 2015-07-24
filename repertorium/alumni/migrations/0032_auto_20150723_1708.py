# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0031_auto_20150723_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='klasfoto',
            name='legende',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, choices=[('email', 'E-mail'), ('linkedin', 'LinkedIn'), ('gsm', 'GSM'), ('twitter', 'Twitter'), ('telefoon', 'Telefoon'), ('website', 'Website')], default='gsm'),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(max_length=10, choices=[('overlijden', 'Overlijden'), ('geboorte', 'Geboorte'), ('huwelijk', 'Huwelijk'), ('overige', 'Overige')], default='geboorte'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, choices=[('M', 'man'), ('A', 'ander'), ('V', 'vrouw'), ('?', 'onbekend')], default='M'),
        ),
    ]
