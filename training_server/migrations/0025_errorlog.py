# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-24 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_server', '0024_auto_20190123_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('step', models.IntegerField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
