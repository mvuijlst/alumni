# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0003_auto_20150718_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='wijzigdatum',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='wijzigdatum',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
