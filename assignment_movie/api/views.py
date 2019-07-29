from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from api.models import Movie, Genre
from api.serializers import MovieSerializer, UserSerializer, GenreSerializer
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Movie View Set
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','year']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

