# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_auto_20150717_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='adres',
            name='wijzigdatum',
            field=models.DateField(default=datetime.datetime(2015, 7, 17, 22, 27, 0, 400926, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='persoon',
            name='wijzigdatum',
            field=models.DateField(default=datetime.datetime(2015, 7, 17, 22, 27, 0, 398924, tzinfo=utc)),
        ),
    ]
