# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.Department'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_code',
            field=models.CharField(max_length=50),
        ),
    ]