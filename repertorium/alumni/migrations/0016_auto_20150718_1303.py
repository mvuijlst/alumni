# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0015_auto_20150718_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beroep',
            name='beroepsgegevens',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, default='gsm', choices=[('linkedin', 'LinkedIn'), ('website', 'Website'), ('gsm', 'GSM'), ('telefoon', 'Telefoon'), ('twitter', 'Twitter')]),
        ),
    ]
