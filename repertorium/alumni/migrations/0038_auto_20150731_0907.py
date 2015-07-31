# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0037_auto_20150731_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacttype',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('naam', models.CharField(max_length=50)),
                ('template', models.CharField(max_length=200)),
                ('actief', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('gsm', 'GSM'), ('website', 'Website'), ('telefoon', 'Telefoon'), ('email', 'E-mail'), ('linkedin', 'LinkedIn')], max_length=10, default='gsm'),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(choices=[('huwelijk', 'Huwelijk'), ('geboorte', 'Geboorte'), ('overige', 'Overige'), ('overlijden', 'Overlijden')], max_length=10, default='geboorte'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(choices=[('A', 'ander'), ('M', 'man'), ('V', 'vrouw'), ('?', 'onbekend')], max_length=1, default='M'),
        ),
    ]
