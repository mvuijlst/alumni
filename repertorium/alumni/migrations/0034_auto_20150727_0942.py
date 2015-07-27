# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0033_auto_20150723_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persoonfoto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('datum', models.DateField(null=True, blank=True)),
                ('foto', models.ImageField(upload_to='klasfoto')),
                ('legende', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': "Personenfoto's",
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, choices=[('email', 'E-mail'), ('telefoon', 'Telefoon'), ('website', 'Website'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('gsm', 'GSM')], default='gsm'),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(max_length=10, choices=[('overige', 'Overige'), ('huwelijk', 'Huwelijk'), ('geboorte', 'Geboorte'), ('overlijden', 'Overlijden')], default='geboorte'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, choices=[('M', 'man'), ('V', 'vrouw'), ('?', 'onbekend'), ('A', 'ander')], default='M'),
        ),
        migrations.AddField(
            model_name='persoonfoto',
            name='persoon',
            field=models.ForeignKey(to='alumni.Persoon'),
        ),
    ]
