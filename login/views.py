from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions

# Create your views here.
from rest_framework.response import Response
from profiles.serializers import UserSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        if user and user.check_password(password):
            authenticate(username=username, password=password)
            serializer = UserSerializer(user)

            return Response(serializer.data)

        return Response()