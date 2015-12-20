from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


# @python_2_unicode_compatible
from gallery.models import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # followers = models.ManyToManyField('self', symmetrical=False)
    rating = models.FloatField(default=0)
    image = models.ForeignKey(Image, null=True, blank=True)

