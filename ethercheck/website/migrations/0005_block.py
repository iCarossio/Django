# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20171220_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockNumber', models.IntegerField(default=0, verbose_name=b'BlockNumber')),
                ('blockHash', models.CharField(blank=True, default=b'', max_length=64, verbose_name=b'BlockHash')),
                ('date', models.DateTimeField(verbose_name=b'Date')),
                ('reward', models.IntegerField(default=0, verbose_name=b'BlockNumber')),
                ('miner', models.CharField(blank=True, default=b'', max_length=64, verbose_name=b'Hash')),
            ],
        ),
    ]
