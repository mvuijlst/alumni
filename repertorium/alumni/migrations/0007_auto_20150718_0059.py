# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0006_auto_20150718_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adres',
            name='wijzigdatum',
        ),
        migrations.RemoveField(
            model_name='persoon',
            name='wijzigdatum',
        ),
        migrations.AddField(
            model_name='adres',
            name='wijziging',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='persoon',
            name='wijziging',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
