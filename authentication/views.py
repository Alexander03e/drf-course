from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from film.serializers import UserSerializer
from rest_framework.response import Response
import django_filters.rest_framework
# from django.contrib.auth.models import User
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import generics
from film.filters import UserEmailFilterBackend
from film.serializers import UserDetailSerializer
from rest_framework import status
# Create your views here.
from film.models import Films

class UserListViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [UserEmailFilterBackend]
    
    def get_queryset(self):
      return self.queryset
    
    def retrieve(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
    
    @action(methods=['POST'], detail=True)
    def add_favorite_movie(self, request, pk):
      user = User.objects.get(id=pk)
      movie_name = request.data.get('movie_name')

      return Response("Фильм успешно добавлен в избранное", status=status.HTTP_201_CREATED)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Сохраняем нового пользователя
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
      queryset=self.get_queryset()
      first_name = request.query_params.get('first')
      last_name = request.query_params.get('last')
      email = request.query_params.get('email')
      

      if first_name:
        queryset = User.objects.filter(
          Q(username__startswith=first_name)
      ) 
      if last_name and first_name:
         queryset = User.objects.filter(
          Q(username__startswith=first_name) & ~Q(username__startswith=last_name) | Q(email=email)
      )
    
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data)
