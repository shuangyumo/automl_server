# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_server', '0007_auto_20190109_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='autokerasconfig',
            name='verbose',
            field=models.BooleanField(default=True),
        ),
    ]
