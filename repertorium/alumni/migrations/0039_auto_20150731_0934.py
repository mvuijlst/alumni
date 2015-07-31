# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0038_auto_20150731_0907'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacttype',
            new_name='Contactmiddel',
        ),
        migrations.AlterModelOptions(
            name='contactmiddel',
            options={'verbose_name_plural': 'Contactmiddelen'},
        ),
        migrations.AddField(
            model_name='contact',
            name='contactmiddel',
            field=models.ForeignKey(default=1, to='alumni.Contactmiddel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='gsm', max_length=10, choices=[('website', 'Website'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('gsm', 'GSM'), ('email', 'E-mail'), ('telefoon', 'Telefoon')]),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(default='geboorte', max_length=10, choices=[('overlijden', 'Overlijden'), ('overige', 'Overige'), ('huwelijk', 'Huwelijk'), ('geboorte', 'Geboorte')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(default='M', max_length=1, choices=[('M', 'man'), ('?', 'onbekend'), ('A', 'ander'), ('V', 'vrouw')]),
        ),
    ]
