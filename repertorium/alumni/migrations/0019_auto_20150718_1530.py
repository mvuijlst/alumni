# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0018_auto_20150718_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', max_length=10, choices=[('website', 'Website'), ('gsm', 'GSM'), ('twitter', 'Twitter'), ('telefoon', 'Telefoon'), ('linkedin', 'LinkedIn')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', max_length=1, choices=[('M', 'man'), ('?', 'onbekend'), ('A', 'ander'), ('V', 'vrouw')]),
        ),
    ]
