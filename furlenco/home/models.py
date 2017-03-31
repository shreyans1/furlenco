from __future__ import unicode_literals

from django.db import models

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=256, default="musicseva")
    playlist_tag = models.CharField(max_length=256, default="musicsevatag")

class Song(models.Model):
    playlist_song = models.ForeignKey(Playlist)
    song_name = models.CharField(max_length=256, default=None)
    song_dur = models.IntegerField(default=0)