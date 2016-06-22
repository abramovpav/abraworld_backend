from django.contrib import admin

# Register your models here.
from music_library.models import Album, Track


class TrackInline(admin.TabularInline):
    model = Track
    extra = 3


class AlbumAdmin(admin.ModelAdmin):

    list_display = ('name', 'publish_at', 'was_published_recently')

    list_filter = ['publish_at']
    search_fields = ['name']

    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    inlines = [TrackInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Track)
