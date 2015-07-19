# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0022_auto_20150719_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='betaling',
            options={'verbose_name_plural': 'Betalingen'},
        ),
        migrations.AddField(
            model_name='betaling',
            name='bedrag',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='betaling',
            name='opmerking',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('linkedin', 'LinkedIn'), ('website', 'Website'), ('twitter', 'Twitter'), ('telefoon', 'Telefoon'), ('gsm', 'GSM')], default='gsm', max_length=10),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('M', 'man'), ('A', 'ander'), ('?', 'onbekend'), ('V', 'vrouw')], default='M', max_length=1),
        ),
    ]
