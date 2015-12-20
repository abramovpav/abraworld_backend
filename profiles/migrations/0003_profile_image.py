# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20151220_1657'),
        ('profiles', '0002_auto_20151220_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ForeignKey(blank=True, to='gallery.Image', null=True),
        ),
    ]
