from rest_framework import serializers

from apps.pizza.serializers import PizzaSerializer
from apps.pizza_shop.models import PizzaShopModel


class PizzaShopSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)
    class Meta:
        model = PizzaShopModel
        fields = ('id', 'name', 'pizzas')
        # depth = 1
