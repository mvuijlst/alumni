# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0032_auto_20150723_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, default='gsm', choices=[('telefoon', 'Telefoon'), ('linkedin', 'LinkedIn'), ('website', 'Website'), ('twitter', 'Twitter'), ('gsm', 'GSM'), ('email', 'E-mail')]),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(max_length=10, default='geboorte', choices=[('overige', 'Overige'), ('overlijden', 'Overlijden'), ('huwelijk', 'Huwelijk'), ('geboorte', 'Geboorte')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, default='M', choices=[('A', 'ander'), ('M', 'man'), ('?', 'onbekend'), ('V', 'vrouw')]),
        ),
    ]
