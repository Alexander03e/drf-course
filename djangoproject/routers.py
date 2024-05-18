from rest_framework import routers
# from authentication.views import UserViewSet
from film.views import FilmsListView 
from serials.views import SerialsListView
from authentication.views import UserListViewSet

router = routers.DefaultRouter()

router.register(r'serials', SerialsListView, basename='serials')
router.register(r'films', FilmsListView, basename='films')
router.register(r'users', UserListViewSet, basename='users')