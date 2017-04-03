from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Playlist_form
from django.contrib import messages


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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Playlist_form(request.POST or None)
        # check whether it's valid:
        if form.is_valid():

            try :
                check = request.POST.get('playlist_name','')
                object = Playlist.objects.get(playlist_name = check)
                return HttpResponseRedirect('/profile/')
            except:
                b = Playlist()
                b.playlist_name = request.POST.get('playlist_name','')
                b.playlist_tag = request.POST.get('playlist_tag', '')
                if request.POST.get('playlist_img_link','')=='':
                    b.playlist_img_link = "http://orig01.deviantart.net/26aa/f/2011/185/f/9/no_cover_itunes_by_stainless2-d3kxnbe.png"

                else:
                    b.playlist_img_link = request.POST.get('playlist_img_link','')
                b.save()
                return HttpResponseRedirect('/profile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Playlist_form()


    return render(request,"profile.html",context)

def create_playlist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Playlist_form(request.POST)
        # check whether it's valid:
        if form.is_valid():


            return HttpResponseRedirect('/profile/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Playlist_form()

    context = {'form':form}
    return render(request,"create_playlist.html",context)


def playlist(request , playlist_name_url):
    if request.method == 'POST':
        url_re = "/playlist/" + playlist_name_url
        link = request.POST.get('song_link','')

        temp = link.split('=')
        try:
            video_id = temp[1]
        except:
            messages.error(request, 'Validation Error  Wrong URL.')
            url_redi = '/playlist/' + playlist_name_url + '/song_add'
            return HttpResponseRedirect(url_redi)
        print (video_id)
        import urllib, json
        url_title = "https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key=AIzaSyCO9HFwW7N6TXdjspvd6wefSuJdMRalW6o&fields=items(snippet(title))&part=snippet"
        response = urllib.urlopen(url_title)
        data = json.loads(response.read())
        data_list = (data['items'])
        if data_list != []:
            dic = data_list[0]
            dic_title = dic['snippet']
            final =  (dic_title['title'])

            a =Song()
            a.playlist_song = playlist_name_url
            a.song_name = final
            a.song_link = link
            a.save()
        else:
            messages.error(request, 'Validation Error Song Does not exist.')
            url_redi = '/playlist/' + playlist_name_url + '/song_add'
            return HttpResponseRedirect(url_redi)







    try:
        songs_all = Song.objects.all()
        object = Playlist.objects.get(playlist_name=playlist_name_url)
        context =  {'playlist_details' :object, 'songs': songs_all,
                    'playlist_name_url':playlist_name_url
                    }

    except:
        return HttpResponse("Error 404")

    return render(request,"playlist.html",context)

def song_add(request,playlist_name_url_2):
    context = {'playlist_name_url_2':playlist_name_url_2}
    return render(request,'song_add.html',context)

def delete_song(request,song_id):
    if request.method == 'POST':
        ob = Song.objects.get(id=song_id)

        ob.delete()
        return HttpResponseRedirect("/profile")



    print(song_id)
    context=  {'song_id':song_id}
    return render(request, 'delete.html',context)


def delete_playlist(request,playlist_id):
    if request.method == 'POST':
        ob = Playlist.objects.get(id=playlist_id)


        ob.delete()
        return HttpResponseRedirect("/profile")

    context = {
        'playlist_id':playlist_id
    }
    return render(request,'delete_playlist.html',context)


def edit_playlist(request,playlist_id):
    b = Playlist.objects.get(id=playlist_id)
    ear_name = b.playlist_name
    if request.method == 'POST':

        b.playlist_name = request.POST.get('playlist_name', '')
        b.playlist_tag = request.POST.get('playlist_tag', '')
        if request.POST.get('playlist_img_link', '') == '':
            b.playlist_img_link = "http://orig01.deviantart.net/26aa/f/2011/185/f/9/no_cover_itunes_by_stainless2-d3kxnbe.png"

        else:
            b.playlist_img_link = request.POST.get('playlist_img_link', '')
        b.save()

        songs_all = Song.objects.all()
        for song in songs_all:
            if song.playlist_song==ear_name:
                song.playlist_song = request.POST.get('playlist_name', '')
                song.save()

        return HttpResponseRedirect('/profile/')



    context = {
        'playlist_id':playlist_id,
        'object':b
    }

    return render(request,'edit_template.html',context)
