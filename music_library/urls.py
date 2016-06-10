from django.conf.urls import url

from music_library import views


app_name = 'music'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^albums$', views.AlbumsView.as_view(), name='albums'),
    url(r'^albums/(?P<pk>[0-9]+)$', views.AlbumView.as_view(), name='album'),
    # url(r'^albums/(?P<album_id>[0-9]+)/tracks$', views.TracksView.as_view(), name='tracks'),
    # url(r'^albums/(?P<album_id>[0-9]+)/tracks/(?P<track_id>[0-9]+)$', views.TrackView.as_view(), name='track'),
    url(r'^albums/(?P<album_id>[0-9]+)/tracks/new$', views.add_track, name='add_track'),

]