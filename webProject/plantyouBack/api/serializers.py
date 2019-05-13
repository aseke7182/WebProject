from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Catalog, Food, Ingredient, Developer, Bonus, Check


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CatalogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    image = serializers.CharField(required=True)

    class Meta:
        model = Catalog
        fields = ('id', 'name', 'image')


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'amount', 'owner',)


class FoodSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    portion = serializers.IntegerField(required=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Food
        fields = ('id', 'name', 'portion', 'owner', 'catalog',)

    def create(self, validated_data):
        catalog = validated_data.pop('catalog')
        return Food.objects.create(catalog=catalog, **validated_data)


class BonusSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    discount = serializers.FloatField(required=True)
    owner = UserSerializer(read_only=True)
    type = serializers.CharField(required=True)


    class Meta:
        model = Bonus
        fields = ('id', 'discount', 'owner', 'type')

class CheckSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    meals = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
    total_price = serializers.FloatField(required=True)

    class Meta:
        model = Check
        fields = ('id', 'meals', 'status', 'total_price')

class DeveloperSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Developer
        fields = ('id', 'name', 'email', 'github', 'phone',)
