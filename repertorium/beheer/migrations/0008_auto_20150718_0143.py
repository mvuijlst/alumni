# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0007_auto_20150718_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='persoon',
            name='geboorteplaats',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='persoon',
            name='overleden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='persoon',
            name='sterfplaats',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
