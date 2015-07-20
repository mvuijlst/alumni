# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0027_auto_20150720_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='opmerking',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('website', 'Website'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('gsm', 'GSM'), ('telefoon', 'Telefoon'), ('email', 'E-mail')], default='gsm', max_length=10),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(choices=[('overlijden', 'Overlijden'), ('geboorte', 'Geboorte'), ('overige', 'Overige'), ('huwelijk', 'Huwelijk')], default='geboorte', max_length=10),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('?', 'onbekend'), ('A', 'ander'), ('M', 'man'), ('V', 'vrouw')], default='M', max_length=1),
        ),
    ]
