# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0034_auto_20150727_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hoedanigheid',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('opmerking', models.CharField(null=True, max_length=100, blank=True)),
                ('van', models.DateField(null=True, blank=True)),
                ('tot', models.DateField(null=True, blank=True)),
                ('geldig', models.BooleanField(default=True)),
                ('wijziging', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hoedanigheden',
            },
        ),
        migrations.CreateModel(
            name='Hoedanigheidstype',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('omschrijving', models.CharField(max_length=50)),
                ('actief', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Soorten hoedanigheden',
            },
        ),
        migrations.AlterModelOptions(
            name='persoonfoto',
            options={'verbose_name_plural': "Foto's"},
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', max_length=10, choices=[('telefoon', 'Telefoon'), ('linkedin', 'LinkedIn'), ('gsm', 'GSM'), ('twitter', 'Twitter'), ('email', 'E-mail'), ('website', 'Website')]),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(default='geboorte', max_length=10, choices=[('overige', 'Overige'), ('overlijden', 'Overlijden'), ('huwelijk', 'Huwelijk'), ('geboorte', 'Geboorte')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', max_length=1, choices=[('A', 'ander'), ('?', 'onbekend'), ('V', 'vrouw'), ('M', 'man')]),
        ),
        migrations.AddField(
            model_name='hoedanigheid',
            name='persoon',
            field=models.ForeignKey(to='alumni.Persoon'),
        ),
        migrations.AddField(
            model_name='hoedanigheid',
            name='hoedanigheidstype',
            field=models.ForeignKey(to='alumni.Hoedanigheidstype'),
        ),
    ]
