# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import alumni.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0021_auto_20150719_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('gsm', 'GSM'), ('telefoon', 'Telefoon'), ('website', 'Website')], default='gsm', max_length=10),
        ),
        migrations.AlterField(
            model_name='klas',
            name='jaar',
            field=models.SmallIntegerField(default=alumni.models.ditjaar),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('A', 'ander'), ('M', 'man'), ('?', 'onbekend'), ('V', 'vrouw')], default='M', max_length=1),
        ),
    ]
