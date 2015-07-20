# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0023_auto_20150719_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gebeurtenis',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('omschrijving', models.TextField()),
                ('datum', models.DateField(blank=True, null=True)),
                ('wijziging', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Gebeurtenissen',
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, default='gsm', choices=[('website', 'Website'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('gsm', 'GSM'), ('telefoon', 'Telefoon')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, default='M', choices=[('V', 'vrouw'), ('A', 'ander'), ('?', 'onbekend'), ('M', 'man')]),
        ),
        migrations.AddField(
            model_name='gebeurtenis',
            name='persoon',
            field=models.ForeignKey(to='alumni.Persoon'),
        ),
    ]
