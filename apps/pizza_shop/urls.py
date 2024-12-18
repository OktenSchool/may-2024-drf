from django.urls import path

from .views import PizzaShopAddPizzaView, PizzaShopListCreateView

urlpatterns = [
    path('', PizzaShopListCreateView.as_view()),
    path('/<int:pk>/pizzas', PizzaShopAddPizzaView.as_view()),
]
