from django.contrib.auth.models import User

from rest_framework import serializers
from gallery.models import Image
from gallery.serializers import ImageSerializer, ReducedImageSerializer
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    image = ReducedImageSerializer()

    class Meta:
        model = Profile


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile')



