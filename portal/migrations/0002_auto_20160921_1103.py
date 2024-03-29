# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('idea_title', models.CharField(max_length=50)),
                ('idea_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='team_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='portal.Team'),
            preserve_default=False,
        ),
    ]
