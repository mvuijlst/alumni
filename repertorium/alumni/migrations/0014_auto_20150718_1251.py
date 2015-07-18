# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0013_auto_20150718_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='beroep',
            name='persoon',
            field=models.ForeignKey(default=1, to='alumni.Persoon'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', max_length=10, choices=[('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('telefoon', 'Telefoon'), ('gsm', 'GSM'), ('website', 'Website')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', max_length=1, choices=[('V', 'vrouw'), ('?', 'onbekend'), ('M', 'man'), ('A', 'ander')]),
        ),
    ]
