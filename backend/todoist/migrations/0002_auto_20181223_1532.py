# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='mark',
            new_name='completed',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='body',
        ),
        migrations.AddField(
            model_name='todo',
            name='text',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
