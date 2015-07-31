# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0036_auto_20150728_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='betalingstype',
            options={},
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, choices=[('telefoon', 'Telefoon'), ('website', 'Website'), ('twitter', 'Twitter'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn'), ('email', 'E-mail')], default='gsm'),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(max_length=10, choices=[('overlijden', 'Overlijden'), ('geboorte', 'Geboorte'), ('overige', 'Overige'), ('huwelijk', 'Huwelijk')], default='geboorte'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, choices=[('A', 'ander'), ('?', 'onbekend'), ('M', 'man'), ('V', 'vrouw')], default='M'),
        ),
    ]
