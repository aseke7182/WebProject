from django.contrib import admin
from api.models import Catalog, Ingredient, Food, Developer, Bonus, Check


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


# @admin.register(Ingredient)
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Ingredient._meta.get_fields()]
#
#
# @admin.register(Food)
# class FoodAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Food._meta.get_fields()]
admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(Check)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Developer._meta.get_fields()]


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bonus._meta.get_fields()]


# @admin.register(Check)
# class CheckAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Check._meta.get_fields()]
