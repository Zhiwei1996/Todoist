# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('expire_time', models.DateTimeField(null=True, blank=True)),
                ('priority', models.IntegerField(blank=True, null=True, choices=[(1, b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa71'), (2, b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa72'), (3, b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa73'), (4, b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa74')])),
                ('mark', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(related_name='todos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_time',),
                'db_table': 'todoist',
            },
        ),
    ]
