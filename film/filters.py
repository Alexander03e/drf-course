import django_filters
from django_filters import rest_framework as filters
from rest_framework import generics, filters, renderers
from .models import Films
from .serializers import FilmsSerializer

class FilmsGenreFilter(django_filters.FilterSet):
  genre = django_filters.CharFilter(field_name='genre')

  class Meta: 
    model = Films
    fields = ['genre']

class GenreFilterBackend(filters.BaseFilterBackend):
  def filter_queryset(self, request,queryset,view):
    genre_parametr = request.query_params.get('genre')

    if genre_parametr: 
      return queryset.filter(genre=genre_parametr)
    return queryset
  
class UserEmailFilterBackend(filters.BaseFilterBackend):
  def filter_queryset(self, request, queryset, view):
    user_email = request.query_params.get('email')

    if user_email: 
      return queryset.filter(email = user_email)
    return queryset
  
