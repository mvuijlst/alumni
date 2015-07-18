# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0008_auto_20150718_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='wijziging',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='wijziging',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
