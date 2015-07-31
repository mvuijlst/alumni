# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import alumni.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0020_auto_20150719_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betaling',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('betalingsjaar', models.IntegerField(blank=True, default=alumni.models.ditjaar, null=True)),
                ('datum', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Betalingstype',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('omschrijving', models.CharField(max_length=50)),
                ('actief', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Soorten betaling',
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, choices=[('website', 'Website'), ('telefoon', 'Telefoon'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter')], default='gsm'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, choices=[('M', 'man'), ('?', 'onbekend'), ('A', 'ander'), ('V', 'vrouw')], default='M'),
        ),
        migrations.AlterField(
            model_name='rhetorica',
            name='jaar',
            field=models.SmallIntegerField(default=alumni.models.ditjaar),
        ),
        migrations.AddField(
            model_name='betaling',
            name='persoon',
            field=models.ForeignKey(to='alumni.Persoon'),
        ),
        migrations.AddField(
            model_name='betaling',
            name='betalingstype',
            field=models.ForeignKey(to='alumni.Betalingstype'),
        ),
    ]
