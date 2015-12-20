from rest_framework import serializers
from gallery.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image


class ReducedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'description')
