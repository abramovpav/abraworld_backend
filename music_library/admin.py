from django.contrib import admin

# Register your models here.
from music_library.models import Album, Track

admin.site.register(Album)
admin.site.register(Track)
