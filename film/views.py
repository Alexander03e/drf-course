from django.shortcuts import render, get_object_or_404, redirect
from .models import Films, Director
from django.views import View
from .serializers import FilmsSerializer
from .serializers import FilmsDetailSerializer
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework import filters
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FilmsGenreFilter
from .filters import GenreFilterBackend
from rest_framework import status
import django_filters

def auth(request):
    return render(request, 'oauth.html')

class FilmsListView(viewsets.ModelViewSet):
    serializer_class = FilmsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'genre', 'rating_stars','year']

    
    def get_queryset(self):
        queryset = Films.objects.all()
        genre_parametr = self.request.query_params.get('genre')
        year_parametr = self.request.query_params.get('year')
        rating_parametr = self.request.query_params.get('rating')
        word_parametr = self.request.query_params.get('word')

        if genre_parametr and year_parametr: 
              queryset = Films.objects.filter(
                Q(genre = genre_parametr) & Q(year = year_parametr) 
              )
        if rating_parametr and word_parametr:
            queryset = Films.objects.filter(
                Q(rating_stars = rating_parametr) & ~Q(is_favorite = False) | Q(title__startswith= word_parametr)
        )     

        return queryset
    

    def retrieve(self, request, pk):
        film = Films.objects.get(id=pk)
        serializer = FilmsDetailSerializer(film)
        return Response(serializer.data)
    
    @action(detail=False, methods = ['GET'])
    def get_favorite_films(self, request):
        favorite_films = Films.objects.filter(is_favorite=True)
        serializer = FilmsSerializer(favorite_films, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        film = Films.objects.get(id=pk)
        film.is_favorite = not film.is_favorite
        film.title = request.data.get('title')
        film.genre = request.data.get('genre')
        film.actors = request.data.get('actors')
        film.subtitle = request.data.get('subtitle')
        film.year = request.data.get('year')
        film.save()
        return Response('Данные обновлены')
    
   








#----------------
        # paginator = LimitOffsetPagination()
        # result_page = paginator.paginate_queryset(queryset, request)
        # serializer = FilmsSerializer(result_page, many = True)
        # return paginator.get_paginated_response(serializer.data)

# class FilmsDetailView(APIView):

#     def get(self, request, pk):
#         film = Films.objects.get(id = pk)
#         serializer = FilmsDetailSerializer(film)
#         return Response(serializer.data)
    
#     @action(detail=False, methods=['GET'] )
#     def get_favorites_films(self, request):
#         films = Films.object.filter(is_favorite=True)
#         serializer = FilmsSerializer(films, many=True   )
#         return Response(serializer.data)
#     # def put(self, request, pk):
#     #     film = get_object_or_404(Films, id = pk)
#     #     serializer = FilmsSerializer(instance = film, data = request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors)
    
#     # def delete(self, request, pk):
#     #     film = get_object_or_404(Films, id = pk)
#     #     film.delete()
#     #     return Response('Film deleted')







