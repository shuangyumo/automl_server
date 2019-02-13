# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-13 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('training', '0002_delete_errorlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='ml_data/prediction_files/')),
                ('result', models.CharField(blank=True, max_length=256, null=True)),
                ('training', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.AutoMlTraining')),
            ],
        ),
    ]
