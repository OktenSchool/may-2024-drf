from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer
from apps.pizza_shop.models import PizzaShopModel
from apps.pizza_shop.serializer import PizzaShopSerializer


class PizzaShopListCreateView(ListCreateAPIView):
    serializer_class = PizzaShopSerializer
    queryset = PizzaShopModel.objects.all()

class PizzaShopAddPizzaView(GenericAPIView):
    queryset = PizzaShopModel.objects.all()

    def post(self, *args, **kwargs):
        pizza_shop = self.get_object()
        data = self.request.data
        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(pizza_shop=pizza_shop)
        shop_serializer = PizzaShopSerializer(pizza_shop)
        return Response(shop_serializer.data, status.HTTP_201_CREATED)
        