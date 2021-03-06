# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-22 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0003_auto_20190122_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiopreprocessor',
            name='evaluation_features_path',
        ),
        migrations.RemoveField(
            model_name='audiopreprocessor',
            name='evaluation_labels_path',
        ),
        migrations.RemoveField(
            model_name='audiopreprocessor',
            name='evaluation_labels_path_binary',
        ),
        migrations.RemoveField(
            model_name='audiopreprocessor',
            name='training_features_path',
        ),
        migrations.RemoveField(
            model_name='audiopreprocessor',
            name='training_labels_path',
        ),
        migrations.RemoveField(
            model_name='audiopreprocessor',
            name='training_labels_path_binary',
        ),
        migrations.AddField(
            model_name='filepreprocessor',
            name='evaluation_features_path',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='filepreprocessor',
            name='evaluation_labels_path',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='filepreprocessor',
            name='evaluation_labels_path_binary',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='filepreprocessor',
            name='training_features_path',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='filepreprocessor',
            name='training_labels_path',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='filepreprocessor',
            name='training_labels_path_binary',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
