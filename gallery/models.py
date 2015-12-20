from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from blog.models import Article


# @python_2_unicode_compatible
class Image(models.Model):
    # post = models.ForeignKey(Article, related_name='photos')
    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=64)
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
