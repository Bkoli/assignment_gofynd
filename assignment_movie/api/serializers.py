from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Movie, Genre


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# Movie Serializer
class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = ('url', 'id', 'title', 'year', 'genre')