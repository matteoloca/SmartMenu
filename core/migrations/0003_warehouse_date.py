# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170610_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]