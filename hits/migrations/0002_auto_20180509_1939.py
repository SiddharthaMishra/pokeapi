# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hits', '0001_squashed_0002_resourceview_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceview',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resourceview',
            name='version',
            field=models.IntegerField(default=1),
        ),
    ]
