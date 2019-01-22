# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-22 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0003_auto_20190122_1302'),
        ('training_server', '0022_auto_20190122_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithmconfig',
            name='load_files_from',
            field=models.CharField(choices=[('preprocessing_job', 'Preprocessing Job Output'), ('filename', 'filename')], default='filename', help_text='Decide wether you want to load your files from a filepath or a grab the output files of a preprocessing job you triggered before', max_length=32),
        ),
        migrations.AddField(
            model_name='algorithmconfig',
            name='preprocessing_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='preprocessing.FilePreprocessor'),
        ),
        migrations.AddField(
            model_name='algorithmconfig',
            name='task_type',
            field=models.CharField(blank=True, choices=[('binary_classification', 'binary classification'), ('multiclass_classification', 'multiclass classification')], help_text='If undefined we automatically perform multiclass classification', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='algorithmconfig',
            name='training_data_filename',
            field=models.CharField(blank=True, default='merged_folds_training_x.npy', help_text='Filename or path to the training data file originating from ml_data folder', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='algorithmconfig',
            name='training_labels_filename',
            field=models.CharField(blank=True, default='merged_folds_training_y.npy', help_text='Filename or path to the training labels file originating from ml_data folder', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='algorithmconfig',
            name='validation_data_filename',
            field=models.CharField(blank=True, default='merged_folds_validation_x.npy', help_text='Filename or path to the validation data file originating from ml_data folder', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='algorithmconfig',
            name='validation_labels_filename',
            field=models.CharField(blank=True, default='merged_folds_validation_y.npy', help_text='Filename or path to the validation labels file originating from ml_data folder', max_length=256, null=True),
        ),
    ]