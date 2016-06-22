from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.db import models


# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


class NameMixin(object):
    @property
    def short_name(self):
        if len(self.name) > 10:
            return self.name[:8] + '...'
        else:
            return self.name

    def was_published_recently(self):
        return datetime.utcnow().date() >= self.publish_at >= (datetime.utcnow() - timedelta(days=1)).date()

    was_published_recently.admin_order_field = 'publish_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


@python_2_unicode_compatible
class Album(models.Model, NameMixin):
    name = models.CharField(max_length=128)
    publish_at = models.DateField()

    def __str__(self):
        return '#{0} {1}'.format(self.id, self.short_name)


@python_2_unicode_compatible
class Track(models.Model, NameMixin):
    name = models.CharField(max_length=256)
    extension = models.CharField(max_length=8)
    size = models.BigIntegerField()
    publish_at = models.DateField()
    album = models.ForeignKey(Album)

    def __str__(self):
        return '#{0} {1}'.format(self.id, self.short_name)
