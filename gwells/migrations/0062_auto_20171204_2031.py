# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-04 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0061_auto_20171204_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='legal_pid',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Property Identification Description (PID)'),
        ),
    ]
