from __future__ import unicode_literals

from django.db import models

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=256, default="musicseva")
    playlist_tag = models.CharField(max_length=256, default="musicsevatag")
    playlist_img_link = models.CharField(max_length=256 , default="http://orig01.deviantart.net/26aa/f/2011/185/f/9/no_cover_itunes_by_stainless2-d3kxnbe.png")
    def __str__(self):
        return self.playlist_name

class Song(models.Model):
    playlist_song = models.CharField(max_length=256,default="NA")
    song_name = models.CharField(max_length=256, default=None)
    song_dur = models.IntegerField(default=0)
    song_link = models.CharField(max_length=256,default=None)
    def __str__(self):
        return self.song_name