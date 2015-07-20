# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0025_auto_20150720_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn'), ('telefoon', 'Telefoon'), ('website', 'Website')], default='gsm', max_length=10),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(choices=[('overlijden', 'Overlijden'), ('huwelijk', 'Huwelijk'), ('overige', 'Overige'), ('geboorte', 'Geboorte')], default='geboorte', max_length=10),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('?', 'onbekend'), ('V', 'vrouw'), ('M', 'man'), ('A', 'ander')], default='M', max_length=1),
        ),
    ]
