from django.urls import path
from . import views

urlpatterns = [
    path('', views.SerialsListView.as_view()),
    path('<int:pk>', views.SerialsDetailView.as_view())
]