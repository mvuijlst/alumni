# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0005_auto_20150718_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rhetorica',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('jaar', models.SmallIntegerField()),
                ('richting', models.CharField(max_length=16)),
                ('titularis', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='persoon',
            name='rhetorica',
            field=models.ForeignKey(null=True, blank=True, to='beheer.Rhetorica'),
        ),
    ]
