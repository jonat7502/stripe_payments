# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 10:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0002_auto_20161109_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 10, 10, 44, 1, 623000, tzinfo=utc)),
        ),
    ]
