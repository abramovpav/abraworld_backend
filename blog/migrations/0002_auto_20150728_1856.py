# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 18, 56, 26, 151814), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 18, 56, 35, 687789), auto_now=True),
            preserve_default=False,
        ),
    ]
