# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170330_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='playlist_img_link',
            field=models.CharField(default='http://orig01.deviantart.net/26aa/f/2011/185/f/9/no_cover_itunes_by_stainless2-d3kxnbe.png', max_length=256),
        ),
        migrations.AddField(
            model_name='song',
            name='song_link',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
