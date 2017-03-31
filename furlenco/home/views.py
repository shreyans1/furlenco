from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Playlist_form
from .models import Playlist,Song

from .models import *
# Create your views here.
def home(request):
    playlist_all = Playlist.objects.all()
    context = {
        'playlist_all':playlist_all
    }
    return render(request,"index.html",context)

def profile(request):
    playlist_all = Playlist.objects.all()
    context = {
        'playlist_all': playlist_all,
    }
    return render(request,"profile.html",context)

def create_playlist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Playlist_form(request.POST)
        # check whether it's valid:
        if form.is_valid():

            #try :
                #object = Playlist.objects.get(playlist_name = form.playlist_name)

            #except:
            b = Playlist()
            b.playlist_name = form.playlist_name
            b.playlist_tag = form.playlist_tag
            b.save()
            print (b)
            return HttpResponseRedirect('/profile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Playlist_form()



    context = {'form':form}
    return render(request,"create_playlist.html",context)












