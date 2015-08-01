# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni', '0039_auto_20150731_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persoon',
            options={'verbose_name_plural': 'Personen', 'ordering': ['-wijziging']},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contacttype',
        ),
        migrations.AddField(
            model_name='persoon',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(max_length=10, default='geboorte', choices=[('overige', 'Overige'), ('overlijden', 'Overlijden'), ('geboorte', 'Geboorte'), ('huwelijk', 'Huwelijk')]),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, default='M', choices=[('?', 'onbekend'), ('V', 'vrouw'), ('A', 'ander'), ('M', 'man')]),
        ),
    ]
