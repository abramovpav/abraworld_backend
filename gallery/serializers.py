from rest_framework import serializers
from gallery.models import Image


class ImageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Image


class CustomImageField(serializers.ImageField):

    def to_representation(self, value):
        if self.use_url:
            if not value:
                return None
            return value.url
        return value.name


class ReducedImageSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    def get_image(self, instance):
        return instance.image.url if instance.image else ''

    class Meta:
        model = Image
        fields = ('id', 'image', 'description')
