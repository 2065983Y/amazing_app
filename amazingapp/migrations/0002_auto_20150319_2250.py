# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amazingapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maze',
            old_name='columns',
            new_name='cols',
        ),
    ]
