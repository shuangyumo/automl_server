# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-22 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the column', max_length=256)),
                ('data_type', models.CharField(choices=[('category', 'category'), ('object', 'object'), ('int', 'int'), ('float', 'float'), ('bool', 'bool'), ('datetime64', 'datetime64'), ('timedelta[ns]', 'timedelta[ns]')], help_text='define the datatype this should be encoded as', max_length=128)),
                ('is_label', models.BooleanField(default=False, help_text='is this a label?')),
            ],
        ),
        migrations.CreateModel(
            name='FilePreprocessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('success', 'Success'), ('fail', 'Fail')], help_text='status of the training', max_length=32, null=True)),
                ('input_file_format', models.CharField(choices=[('parquet', 'parquet'), ('png', 'png'), ('wav', 'wav')], help_text='format of the input data', max_length=16)),
                ('output_file_format', models.CharField(choices=[('npy', 'npy'), ('csv', 'csv'), ('pkl', 'pkl')], help_text='format of the output data', max_length=16)),
                ('additional_remarks', models.CharField(blank=True, help_text='Additional Information about the training. E.g. Information about failed trainings are logged here in case a training fails!', max_length=2048, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AudioPreprocessor',
            fields=[
                ('filepreprocessor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='preprocessing.FilePreprocessor')),
                ('folder_name', models.CharField(blank=True, default='/wav/', max_length=256, null=True)),
                ('transform_categorical_to_binary', models.BooleanField(default=False)),
                ('binary_true_name', models.CharField(blank=True, default='no_fat_behavior', max_length=256, null=True)),
            ],
            bases=('preprocessing.filepreprocessor',),
        ),
        migrations.AddField(
            model_name='column',
            name='file_reformater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preprocessing.FilePreprocessor'),
        ),
    ]
