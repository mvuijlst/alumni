# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0035_auto_20150728_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='soorthoedanigheid',
            options={'verbose_name_plural': 'Hoedanigheden', 'verbose_name': 'Hoedanigheid'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(max_length=10, choices=[('telefoon', 'Telefoon'), ('website', 'Website'), ('gsm', 'GSM'), ('email', 'E-mail'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter')], default='gsm'),
        ),
        migrations.AlterField(
            model_name='gebeurtenis',
            name='gebeurtenistype',
            field=models.CharField(max_length=10, choices=[('overige', 'Overige'), ('huwelijk', 'Huwelijk'), ('geboorte', 'Geboorte'), ('overlijden', 'Overlijden')], default='geboorte'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='geslacht',
            field=models.CharField(max_length=1, choices=[('M', 'man'), ('?', 'onbekend'), ('V', 'vrouw'), ('A', 'ander')], default='M'),
        ),
        migrations.AlterField(
            model_name='persoon',
            name='voornaam',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
