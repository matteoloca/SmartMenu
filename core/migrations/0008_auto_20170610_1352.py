# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170610_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productwithrecipe',
            name='is_course',
        ),
        migrations.AddField(
            model_name='productwithrecipe',
            name='kind',
            field=models.SmallIntegerField(choices=[(1, 'Piatto'), (2, 'Preparato')], default=1),
        ),
    ]
