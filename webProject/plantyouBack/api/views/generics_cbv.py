from rest_framework import generics, filters
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import Http404
from api.serializers import UserSerializer, CatalogSerializer, FoodSerializer, IngredientSerializer
from api.models import Catalog, Food, Ingredient
from rest_framework.response import Response


# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# from django_filters.rest_framework import DjangoFilterBackend
# from api.filters import TaskFilter


class CatalogList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()


class CatalogInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatalogSerializer
    permission_classes = (IsAdminUser,)
    queryset = Catalog.objects.all()


class IngredientList(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()


class IngredientInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()


class FoodList(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        catalog = get_object_or_404(Catalog, id=self.kwargs.get('pk'))
        queryset = catalog.foods.all()
        # queryset = queryset.objects.for_user()
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FoodInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'pk2'

    def get_queryset(self):
        catalog = get_object_or_404(Catalog, id=self.kwargs.get('pk'))
        queryset = catalog.foods.filter(owner=self.request.user)
        return queryset
