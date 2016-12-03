# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-03 16:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20161203_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anevent',
            name='end_time',
            field=models.TimeField(default=datetime.time(0, 0), help_text='ex: 13:30 for 1:30 PM'),
        ),
        migrations.AlterField(
            model_name='anevent',
            name='start_time',
            field=models.TimeField(default=datetime.time(0, 0), help_text='ex: 10:30 for 10:30 AM'),
        ),
    ]