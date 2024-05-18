from django.urls import path, include
from . import views

# from rest_framework import routers

urlpatterns = [
    path('', views.FilmsListView.as_view()),
    path('<int:pk>/', views.FilmsDetailView.as_view()), 
    
]

