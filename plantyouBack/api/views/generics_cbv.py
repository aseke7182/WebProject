from rest_framework import generics, filters
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from api.models import Catalog, Food
from api.serializers import UserSerializer, CatalogSerializer, FoodSerializer

# from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from api.models import Catalog, Food
from api.serializers import UserSerializer, CatalogSerializer


# from django_filters.rest_framework import DjangoFilterBackend


# from api.filters import TaskFilter


class CatalogList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    permission_classes = (IsAdminUser,)
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()


class CatalogInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatalogSerializer
    permission_classes = (IsAdminUser,)
    queryset = Catalog.objects.all()


class FoodList(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        catalog = get_object_or_404(Catalog, id=self.kwargs.get('pk'))
        queryset = catalog.foods.filter(owner=self.request.user)
        return queryset
