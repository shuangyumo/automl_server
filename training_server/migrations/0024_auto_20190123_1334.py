# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-23 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0006_auto_20190123_1334'),
        ('training_server', '0023_auto_20190122_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='AlgorithmConfig',
            name='preprocessing_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='preprocessing.FilePreprocessor'),
        ),
    ]
