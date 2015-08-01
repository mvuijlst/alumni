# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0040_auto_20150801_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='persoon',
            name='wikipedia',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(max_length=10, default='geboorte', choices=[('huwelijk', 'Huwelijk'), ('overlijden', 'Overlijden'), ('overige', 'Overige'), ('geboorte', 'Geboorte')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, default='M', choices=[('?', 'onbekend'), ('A', 'ander'), ('M', 'man'), ('V', 'vrouw')]),
        ),
    ]
