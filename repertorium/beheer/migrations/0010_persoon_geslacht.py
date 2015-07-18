# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0009_auto_20150718_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', choices=[('A', 'ander'), ('M', 'man'), ('?', 'onbekend'), ('V', 'vrouw')], max_length=1),
        ),
    ]
