# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 05:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserSignUp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='user',
        ),
        migrations.DeleteModel(
            name='user_info',
        ),
    ]