# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0003_intradepackage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blackcatpackage',
            old_name='blakcat_id',
            new_name='blackcat_id',
        ),
    ]
