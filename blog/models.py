from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# @python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
