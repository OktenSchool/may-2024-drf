from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer, PizzaPhotoSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)
    # pagination_class = None

    # def get_queryset(self):
    #     request:Request = self.request
    #     return filter_pizza(request.query_params)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'delete']

class PizzaAddPhotoView(UpdateAPIView):
    serializer_class = PizzaPhotoSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['put']
    permission_classes = (AllowAny,)

    def perform_update(self, serializer):
        pizza = self.get_object()
        pizza.photo.delete()
        super().perform_update(serializer)


