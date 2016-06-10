from django.conf.urls import url

from music_library import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]