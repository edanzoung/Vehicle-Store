# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20210202_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicules',
            name='date',
            field=models.CharField(max_length=100, blank=True, default='4/2/2021'),
        ),
    ]
