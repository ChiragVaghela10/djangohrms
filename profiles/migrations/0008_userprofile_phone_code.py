# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-11 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_userprofile_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_code',
            field=models.CharField(choices=[('IN', 'in'), ('US', 'us')], default='', max_length=2),
        ),
    ]
