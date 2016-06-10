# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('publish_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('extension', models.CharField(max_length=8)),
                ('size', models.BigIntegerField()),
                ('publish_at', models.DateField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_library.Album')),
            ],
        ),
    ]
