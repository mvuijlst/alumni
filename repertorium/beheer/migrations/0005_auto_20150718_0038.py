# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0004_auto_20150718_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='tot',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adres',
            name='van',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geboortedatum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='oudid',
            field=models.IntegerField(verbose_name='tnr_oudleerling uit oude db', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='sterfdatum',
            field=models.DateField(blank=True, null=True),
        ),
    ]
