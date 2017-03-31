from django import forms
from .models import Playlist,Song

class Playlist_form(forms.Form):
    playlist_name = forms.CharField(max_length=256)
    playlist_tag = forms.CharField(max_length=256)
