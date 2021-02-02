from foodApp.settings import REST_FRAMEWORK
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import*
from .serializers import*


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ApiSerializer


class APIRoot(generics.GenericAPIView):
    def get(self, request):
        api_urls = {
            'Post APIs': '/posts/',
            'User Resistration': '/dj-rest-auth/registration/',
            'User Login': '/dj-rest-auth/login/',
            'User Logout': '/dj-rest-auth/logout/',
            'User Password Change': '/dj-rest-auth/password/change/',
            'User Details': '/dj-rest-auth/user/',
            'Token Verify': '/dj-rest-auth/token/verify/',
            'Token Refresh Using Dj-rest-auth': '/dj-rest-auth/token/refresh/',
            'Token Access Using Simple JWt': '/api/token/',
            'Token Refresh Using Simple JWT': '/api/token/refresh/',
        }
        return Response(api_urls)
