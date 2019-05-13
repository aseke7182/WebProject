from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class FoodManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class Catalog(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, default="1")

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'

    def __str__(self):
        return '{}: {} {}'.format(self.id, self.name, self.image)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image
        }


class Food(models.Model):
    name = models.CharField(max_length=200)
    portion = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT, related_name='foods')
    objects = FoodManager()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': id,
            'name': self.name,
            'portion': self.portion,
            'owner': self.owner,
            'catalog': self.catalog,
            'objects': self.objects
        }


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    foods = models.ForeignKey(Food, on_delete=models.CASCADE, default=11, related_name='ingredients')

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': id,
            'name': self.name,
            'amount': self.amount,
            'owner': self.owner,
            'foods': self.foods
        }


class Check(models.Model):
    STATUS_ORDERS = (
        ('DONE', 'Done'),
        ('IN PROCESS', 'In process'),
        ('UNDONE', 'Undone'),
    )
    meals = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUS_ORDERS, default='UNDONE')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    handler = models.ForeignKey(User, on_delete=models.CASCADE, related_name='handler')
    total_price = models.FloatField(default=0)


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
    type = models.CharField(max_length=8, choices=TYPE_ORDERS, default='FREE')

    def str(self):
        return "{} {}".format(self.type, self.owner)

    def to_json(self):
        return {
            'id': self.id,
            'discount': self.discount,
            'owner': self.owner,
            'type': self.type,
            'start_date': self.start_date,
            'end_date': self.end_date,
        }
    class Meta:
        verbose_name_plural= 'Bonuses'

class Developer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    phone = models.IntegerField()
