from django.contrib.auth.models import User
from rest_framework import serializers
from recruitment_app.models import LongURL


class UserSerializer(serializers.HyperlinkedModelSerializer):
    longurl = serializers.HyperlinkedRelatedField(many=True, view_name='Longurl-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'email', 'password', 'date_joined', 'longurl']

#Craete serializer for AddURL
class AddURLSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LongURL
        fields = ['id', 'owner', 'created', 'longurl']


#Create serializer for ShortURL
class ShortURLSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model =LongURL
        fields = ['id', 'owner', 'created', 'longurl', 'shorturl']