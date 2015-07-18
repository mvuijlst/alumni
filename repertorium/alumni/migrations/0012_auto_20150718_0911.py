# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0011_auto_20150718_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='rhetorica',
            name='jaar',
            field=models.SmallIntegerField(default=2015),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, default='gsm', choices=[('gsm', 'GSM'), ('linkedin', 'LinkedIn'), ('website', 'Website'), ('telefoon', 'Telefoon')]),
        ),
        migrations.AlterField(
            model_name='klas',
            name='jaar',
            field=models.SmallIntegerField(default=2015),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, default='M', choices=[('A', 'ander'), ('?', 'onbekend'), ('M', 'man'), ('V', 'vrouw')]),
        ),
    ]
