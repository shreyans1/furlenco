# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='musicseva', max_length=256)),
                ('tag', models.CharField(default='musicsevatag', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Playlist')),
            ],
        ),
    ]
