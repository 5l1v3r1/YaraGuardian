# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-02 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yararule',
            name='category',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='yararule',
            name='source',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]
