# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_participant_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='idea_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='team',
            name='idea_title',
            field=models.CharField(max_length=100),
        ),
    ]
