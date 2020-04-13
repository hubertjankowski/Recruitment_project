from sqlite3 import IntegrityError

from django.contrib.auth.models import User
from django.db.migrations import serializer
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from recruitment_app.delete_first_sign import delete_first_sign
from recruitment_app.permissions import IsOwnerOrReadOnly
from recruitment_app.models import LongURL
from recruitment_app.serializers import UserSerializer, AddURLSerializer, ShortURLSerializer
from recruitment_app.get_random_user import random_user



# Create view for users
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create view for ShortURL
class ShortURLViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LongURL.objects.all()
    serializer_class = ShortURLSerializer

#Create view for URL like "www.example.com/test" and "www.example.com/!test"
@api_view(['GET'])
def url_detail(request, shorturl):
    if shorturl[0] == "!":
        new_shorturl = delete_first_sign(shorturl)
        try:
            object_detail = LongURL.objects.get(shorturl=new_shorturl)
        except LongURL.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ShortURLSerializer(object_detail)
            return Response(serializer.data)
    else:
        full_length = get_object_or_404(LongURL, shorturl=shorturl).longurl
        return HttpResponseRedirect(full_length)


# Create view for AddURL
class AddURLViewSet(viewsets.ModelViewSet):
    queryset = LongURL.objects.all()
    serializer_class = AddURLSerializer

    #Chceck database if the URL does not repeat
    def perform_create(self, serializer):
        try:
            if serializer.is_valid(raise_exception=False):
                serializer.save(owner=random_user())
        except IntegrityError:
            return Response(data={'message': 'That URL already exists'}, status=HTTP_400_BAD_REQUEST)
