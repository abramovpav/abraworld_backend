from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from music_library.models import Album, Track


def index(request):
    context = {
        'latest_albums_list': Album.objects.all()[:5]
    }
    return render(request, 'music_library/index.html', context)


class AlbumsView(generic.ListView):
    template_name = 'music_library/albums.html'
    context_object_name = 'latest_albums_list'

    def get_queryset(self):
        return Album.objects.order_by('-publish_at').all()[:5]


class AlbumView(generic.DetailView):
    template_name = 'music_library/album.html'
    model = Album


class TracksView(generic.ListView):
    template_name = 'music_library/trucks.html'
    context_object_name = 'tracks'

    def get_queryset(self):
        return Track.objects.all()


class TrackView(generic.DetailView):
    template_name = 'music_library/track.html'
    model = Track


def add_track(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        track = album.track_set.create(
            name=request.POST['name'],
            extension=request.POST['extension'],
            size=1024,
            publish_at=datetime.utcnow()
        )
    except (KeyError, ):
        return render(request, 'music_library/album.html', {'album': album, 'error_message': 'invalid fields'})
    return HttpResponseRedirect(reverse('music:album', args=(album_id,)))
