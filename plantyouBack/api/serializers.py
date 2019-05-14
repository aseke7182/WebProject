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
    amounts = serializers.IntegerField(required=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'amounts',)


class FoodSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    ingredients = IngredientSerializer(read_only=True, many=True)
    # ingr = IngredientSerializer(write_only=True, many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Food
        fields = ('id', 'name', 'portion', 'owner', 'catalog', 'price', 'ingredients', 'ingr')

    def create(self, validated_data):
        catalog = validated_data.pop('catalog')
        ingredients = validated_data.pop('ingr')
        instance = Food.objects.create(catalog=catalog, **validated_data)
        instance.ingredients.set(ingredients)
        return instance


class CheckSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True)
    foods = FoodSerializer(read_only=True, many=True)

    class Meta:
        model = Check
        fields = ('id', 'status', 'cost', 'owner', 'foods', 'fo')

    def create(self, validated_data):
        foods = validated_data.pop('fo')
        cost = 0
        for i in foods:
            cost += i.price
        instance = Check.objects.create(cost=cost, **validated_data)
        instance.foods.set(foods)
        return instance


class DeveloperSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Developer
        fields = ('id', 'name', 'email', 'github', 'phone',)


class BonusSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    discount = serializers.FloatField(required=True)
    owner = UserSerializer(read_only=True)
    type = serializers.CharField(required=True)

    class Meta:
        model = Bonus
        fields = ('id', 'discount', 'owner', 'type')
