# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0016_auto_20150718_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adres',
            options={'verbose_name_plural': 'Adressen'},
        ),
        migrations.AlterModelOptions(
            name='beroep',
            options={'verbose_name_plural': 'Beroepen'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contactmiddelen'},
        ),
        migrations.AlterModelOptions(
            name='klas',
            options={'verbose_name_plural': 'Klassen'},
        ),
        migrations.AlterModelOptions(
            name='klasfoto',
            options={'verbose_name_plural': "Klasfoto's"},
        ),
        migrations.AlterModelOptions(
            name='persoon',
            options={'verbose_name_plural': 'Personen'},
        ),
        migrations.AlterModelOptions(
            name='rhetorica',
            options={'verbose_name_plural': "Rhetorica's"},
        ),
        migrations.AddField(
            model_name='klasfoto',
            name='datum',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('gsm', 'GSM'), ('linkedin', 'LinkedIn'), ('website', 'Website'), ('telefoon', 'Telefoon')], default='gsm', max_length=10),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('?', 'onbekend'), ('A', 'ander'), ('V', 'vrouw'), ('M', 'man')], default='M', max_length=1),
        ),
    ]
