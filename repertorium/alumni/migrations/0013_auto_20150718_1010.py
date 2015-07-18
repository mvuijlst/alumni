# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0012_auto_20150718_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='persoon',
            name='opmerkingen',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', choices=[('website', 'Website'), ('telefoon', 'Telefoon'), ('twitter', 'Twitter'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn')], max_length=10),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', choices=[('?', 'onbekend'), ('A', 'ander'), ('V', 'vrouw'), ('M', 'man')], max_length=1),
        ),
    ]
