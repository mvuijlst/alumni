# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0029_auto_20150721_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', max_length=10, choices=[('email', 'E-mail'), ('twitter', 'Twitter'), ('telefoon', 'Telefoon'), ('gsm', 'GSM'), ('website', 'Website'), ('linkedin', 'LinkedIn')]),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(default='geboorte', max_length=10, choices=[('geboorte', 'Geboorte'), ('huwelijk', 'Huwelijk'), ('overige', 'Overige'), ('overlijden', 'Overlijden')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', max_length=1, choices=[('?', 'onbekend'), ('A', 'ander'), ('V', 'vrouw'), ('M', 'man')]),
        ),
    ]
