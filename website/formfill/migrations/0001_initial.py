# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100, null=True, blank=True)),
                ('contact', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'course',
            },
        ),
    ]
