# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 02:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrator', '0005_auto_20171001_0222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investor',
            old_name='user',
            new_name='users',
        ),
    ]
