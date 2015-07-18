# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0014_auto_20150718_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', max_length=10, choices=[('twitter', 'Twitter'), ('telefoon', 'Telefoon'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn'), ('website', 'Website')]),
        ),
    ]
