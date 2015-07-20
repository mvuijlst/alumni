# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0028_auto_20150720_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('email', 'E-mail'), ('website', 'Website'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('gsm', 'GSM'), ('telefoon', 'Telefoon')], max_length=10, default='gsm'),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(choices=[('huwelijk', 'Huwelijk'), ('overige', 'Overige'), ('geboorte', 'Geboorte'), ('overlijden', 'Overlijden')], max_length=10, default='geboorte'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('?', 'onbekend'), ('M', 'man'), ('V', 'vrouw'), ('A', 'ander')], max_length=1, default='M'),
        ),
    ]
