# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-24 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umiss_auth', '0006_auto_20170519_1737'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MonitorUser',
            new_name='Monitor',
        ),
    ]
