# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_editor', '0002_auto_20170502_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='from_question',
            new_name='on_question',
        ),
    ]
