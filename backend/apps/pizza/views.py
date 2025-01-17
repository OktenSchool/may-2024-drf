from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.utils.decorators import method_decorator
from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer, PizzaPhotoSerializer, PizzaResponseSerializer
from drf_yasg.utils import swagger_auto_schema
@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[],
        operation_description='Hahaha',
        responses={200: PizzaResponseSerializer()},
        operation_summary='get all piizas'
    )
)
class PizzaListCreateView(ListCreateAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)
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


