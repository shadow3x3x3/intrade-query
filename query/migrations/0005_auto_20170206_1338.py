# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0004_auto_20170111_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intradepackage',
            old_name='blackcat_id',
            new_name='blackcat',
        ),
        migrations.RenameField(
            model_name='intradepackage',
            old_name='chinese_id',
            new_name='chinese',
        ),
    ]
