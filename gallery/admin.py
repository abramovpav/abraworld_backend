from django.contrib import admin

admin.autodiscover()

# Register your models here.
from gallery.models import Image


class ImageAdmin(admin.ModelAdmin):
    fields = ('image', 'description', 'owner', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Image, ImageAdmin)
