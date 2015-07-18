# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('adres', models.TextField()),
                ('van', models.DateField()),
                ('tot', models.DateField()),
                ('geldig', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persoon',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('voornaam', models.CharField(max_length=200)),
                ('achternaam', models.CharField(max_length=200)),
                ('geboortedatum', models.DateField()),
                ('sterfdatum', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='adres',
            name='persoon',
            field=models.ForeignKey(to='alumni.Persoon'),
        ),
    ]
