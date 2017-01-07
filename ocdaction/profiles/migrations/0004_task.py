# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-01 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_ocdactionuser_have_ocd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('is_archived', models.BooleanField(default=False)),
            ],
        ),
    ]
