# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-18 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_server', '0009_auto_20190113_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithmconfig',
            name='training_time',
            field=models.CharField(blank=True, help_text='training time until completion or interrupt (in seconds)', max_length=128, null=True),
        ),
    ]
