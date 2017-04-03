from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^profile/', views.profile),
    url(r'^create_playlist/', views.create_playlist),
    url(r'^playlist/(?P<playlist_name_url>[ A-Za-z0-9_@./#&+-]*)/$', views.playlist),
    url(r'^playlist/(?P<playlist_name_url_2>[ A-Za-z0-9_@./#&+-]*)/song_add', views.song_add),
    url(r'^(?P<song_id>[0-9]+)/delete', views.delete_song),
    url(r'^playlist_delete/(?P<playlist_id>[0-9]+)/delete', views.delete_playlist),
    url(r'^playlist_edit/(?P<playlist_id>[0-9]+)/edit', views.edit_playlist),
]
