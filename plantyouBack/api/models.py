from django.db import models
from django.contrib.auth.models import User


class FoodManager(models.Manager):
    def for_user(self, user):
        Food.objects.filter(owner=user)


class Catalog(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, default="1")


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Food(models.Model):
    name = models.CharField(max_length=200)
    portion = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT, related_name='foods')
    objects = FoodManager()

# TODO How Should We Do It ?
# class Check(models.Model):
#     price = models.IntegerField()
#     data = models.DateTimeField(auto_now=True)
#     address = models.CharField()
#     foods = models.ForeignKey(Food, on_delete=models.SET_NULL())
