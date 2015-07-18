# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0010_persoon_geslacht'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beroep',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('beroepsgegevens', models.TextField()),
                ('van', models.DateField(blank=True, null=True)),
                ('tot', models.DateField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('wijziging', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('contacttype', models.CharField(choices=[('gsm', 'GSM'), ('linkedin', 'LinkedIn'), ('telefoon', 'Telefoon'), ('website', 'Website')], max_length=10, default='gsm')),
                ('contactdata', models.CharField(max_length=200)),
                ('van', models.DateField(blank=True, null=True)),
                ('tot', models.DateField(blank=True, null=True)),
                ('geldig', models.BooleanField(default=True)),
                ('wijziging', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Klas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('jaar', models.SmallIntegerField()),
                ('klasnaam', models.CharField(blank=True, max_length=50, null=True)),
                ('titularis', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Klasfoto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='klasfoto')),
                ('klas', models.ForeignKey(to='beheer.Klas')),
            ],
        ),
        migrations.RemoveField(
            model_name='rhetorica',
            name='jaar',
        ),
        migrations.RemoveField(
            model_name='rhetorica',
            name='titularis',
        ),
        migrations.AddField(
            model_name='persoon',
            name='contacteren',
            field=models.BooleanField(verbose_name='mag gecontacteerd worden?', default=True),
        ),
        migrations.AddField(
            model_name='persoon',
            name='klasvertegenwoordiger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='persoon',
            name='publiek',
            field=models.BooleanField(verbose_name='mag online verschijnen?', default=True),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('V', 'vrouw'), ('M', 'man'), ('?', 'onbekend'), ('A', 'ander')], max_length=1, default='M'),
        ),
        migrations.AddField(
            model_name='contact',
            name='persoon',
            field=models.ForeignKey(to='beheer.Persoon'),
        ),
        migrations.AddField(
            model_name='rhetorica',
            name='klas',
            field=models.ForeignKey(blank=True, to='beheer.Klas', null=True),
        ),
    ]
