# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 15:15
from __future__ import unicode_literals

import admission.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='Registree',
            new_name='registree',
        ),
        migrations.AlterField(
            model_name='registration',
            name='registration_number',
            field=models.CharField(default=admission.models.registration_number, editable=False, max_length=16, unique=True),
        ),
    ]