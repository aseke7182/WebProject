from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class FoodManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class Catalog(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, default="1")


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amounts = models.IntegerField()


class Food(models.Model):
    name = models.CharField(max_length=200)
    portion = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT, related_name='foods')
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')
    ingr = models.ManyToManyField(Ingredient)
    price = models.IntegerField(default=500)
    objects = FoodManager()


class Check(models.Model):
    STATUS_ORDERS = (
        ('DONE', 'Done'),
        ('IN PROCESS', 'In process'),
        ('UNDONE', 'Undone'),
    )
    status = models.CharField(max_length=10, choices=STATUS_ORDERS, default='UNDONE')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    cost = models.FloatField(default=0)
    foods = models.ManyToManyField(Food, related_name='food')
    fo = models.ManyToManyField(Food)


class Bonus(models.Model):
    TYPE_ORDERS = (
        ('PREMIUM', 'premium'),
        ('STANDART', 'standart'),
        ('STANDART+', 'standart+'),
        ('FREE', 'free')
    )

    discount = models.FloatField(default=5)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    type = models.CharField(max_length=80, choices=TYPE_ORDERS, default='FREE')

    class Meta:
        verbose_name_plural = 'Bonuses'


class Developer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    phone = models.IntegerField()
