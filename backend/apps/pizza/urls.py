from django.urls import path
from .views import PizzaListCreateView, PizzaRetrieveUpdateDestroyView, PizzaAddPhotoView
urlpatterns = [
    path("", PizzaListCreateView.as_view()),
    path("/<int:pk>", PizzaRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/photos", PizzaAddPhotoView.as_view()),

]
