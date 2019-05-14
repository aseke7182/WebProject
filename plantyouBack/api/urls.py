from django.urls import path
from api import views

urlpatterns = [
    path('catalogs/', views.CatalogList.as_view()),
    path('catalogs/<int:pk>/', views.CatalogInfo.as_view()),
    path('catalogs/<int:pk>/foods/', views.FoodList.as_view()),
    path('catalogs/<int:pk>/foods/<int:pk2>/', views.FoodInfo.as_view()),
    path('ingredients/', views.IngredientList.as_view()),
    path('ingredients/<int:pk>/', views.IngredientInfo.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('signup/', views.create_user),
    path('users/', views.UserList.as_view()),
    path('developers/', views.Developers.as_view()),
    path('developers/<int:pk>/', views.DeveloperInfo.as_view()),
    path('checks/', views.CheckList.as_view()),
    path('userfoods/<int:pk>/', views.UsersFoodList.as_view()),
]
