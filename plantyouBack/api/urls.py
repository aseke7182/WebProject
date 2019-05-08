from django.urls import path
from api import views

urlpatterns = [
    path('catalogs/', views.CatalogList.as_view()),
    path('catalogs/<int:pk>/', views.CatalogInfo.as_view()),
    path('catalogs/<int:pk>/foods/', views.FoodList.as_view()),
    # path('ingredients/', views.IngredientList.as_view()),
    # path('ingredients/<int:pk>/', views.IngredientInfo.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('signup/', views.create_user),
    path('users/', views.UserList.as_view()),
]
