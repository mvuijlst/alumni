# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0030_auto_20150721_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', max_length=10, choices=[('twitter', 'Twitter'), ('telefoon', 'Telefoon'), ('email', 'E-mail'), ('website', 'Website'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn')]),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(default='geboorte', max_length=10, choices=[('overige', 'Overige'), ('geboorte', 'Geboorte'), ('huwelijk', 'Huwelijk'), ('overlijden', 'Overlijden')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', max_length=1, choices=[('M', 'man'), ('?', 'onbekend'), ('V', 'vrouw'), ('A', 'ander')]),
        ),
    ]
