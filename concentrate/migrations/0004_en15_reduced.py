# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrate', '0003_auto_20170324_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='en15',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='reduced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
            ],
        ),
    ]
