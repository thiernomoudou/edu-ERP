# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='school_adress_one',
            new_name='adress_1',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_adress_two',
            new_name='adress_2',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_authorization_number',
            new_name='authorization_number',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_fax',
            new_name='fax',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_registry',
            new_name='registration_number',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_slogan',
            new_name='slogan',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_tax_id',
            new_name='tax_id',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='school_website',
            new_name='website',
        ),
    ]
