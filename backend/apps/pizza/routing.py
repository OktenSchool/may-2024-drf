from django.urls import path

from apps.pizza.consumer import PizzaConsumer

websocket_urlpatterns = [
    path('', PizzaConsumer.as_asgi()),
]
