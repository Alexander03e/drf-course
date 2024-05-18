from django.shortcuts import render, get_object_or_404,redirect
from .models import Serials
from rest_framework import generics
from .serializers import SerialsSerializer
from .serializers import SerialsDetailSerializer
from rest_framework import viewsets,routers,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
def serials(request):
    serials = Serials.objects.all()
    return render(request, "serials/object.html", {'serials': serials})


class SerialsListView(viewsets.ModelViewSet):
    queryset = Serials.objects.all()
    serializer_class = SerialsSerializer

    def retrieve(self, request, pk):
        serial = Serials.objects.get(id=pk)
        serializer = SerialsDetailSerializer(serial)
        return Response(serializer.data)

    @action(detail=False, methods = ['GET'])
    def get_favorite_serials(self, request):
        favorite_serials = Serials.objects.filter(is_favorite=True)
        serializer = SerialsSerializer(favorite_serials, many=True)
        return Response(serializer.data)


#--------------------------------------------------#
#     http_method_names = ['get']
#     # def get(self, request):
#     #     queryset = Serials.objects.all()
#     #     serializer = SerialsSerializer(queryset, many = True)
#     #     return Response(serializer.data)
    

# class SerialsDetailView(APIView):

#     def get(self, request, pk):
#         serial = Serials.objects.get(id = pk)
#         serializer = SerialsDetailSerializer(serial)
#         return Response(serializer.data)