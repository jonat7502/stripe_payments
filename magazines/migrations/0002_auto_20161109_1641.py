# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 16:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 9, 16, 41, 18, 680000, tzinfo=utc)),
        ),
    ]