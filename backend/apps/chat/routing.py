from django.urls import path
from .cunsumers import ChatConsumer

websocket_urlpatterns = [
    path('<str:room>/', ChatConsumer.as_asgi())
]
