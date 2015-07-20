# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0026_auto_20150720_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persoon',
            name='email',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', max_length=10, choices=[('website', 'Website'), ('gsm', 'GSM'), ('telefoon', 'Telefoon'), ('email', 'E-mail'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn')]),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(default='geboorte', max_length=10, choices=[('overige', 'Overige'), ('overlijden', 'Overlijden'), ('geboorte', 'Geboorte'), ('huwelijk', 'Huwelijk')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', max_length=1, choices=[('V', 'vrouw'), ('A', 'ander'), ('?', 'onbekend'), ('M', 'man')]),
        ),
    ]
