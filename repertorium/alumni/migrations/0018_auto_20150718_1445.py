# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0017_auto_20150718_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', choices=[('telefoon', 'Telefoon'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn'), ('website', 'Website'), ('twitter', 'Twitter')], max_length=10),
        ),
        migrations.AlterField(
            model_name='klasfoto',
            name='datum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', choices=[('A', 'ander'), ('?', 'onbekend'), ('V', 'vrouw'), ('M', 'man')], max_length=1),
        ),
    ]
