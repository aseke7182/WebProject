from django.contrib import admin
from api.models import Catalog, Ingredient, Food, Developer


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ingredient._meta.get_fields()]


# admin.register(Food)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.get_fields()]


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Developer._meta.get_fields()]
