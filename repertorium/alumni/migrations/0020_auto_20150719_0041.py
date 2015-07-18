# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0019_auto_20150718_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('telefoon', 'Telefoon'), ('gsm', 'GSM'), ('website', 'Website')], default='gsm', max_length=10),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('?', 'onbekend'), ('M', 'man'), ('A', 'ander'), ('V', 'vrouw')], default='M', max_length=1),
        ),
    ]
