# from django.db.models import QuerySet
# from django.http import QueryDict
#
# from rest_framework.exceptions import (
#     APIException,
#     AuthenticationFailed,
#     NotAcceptable,
#     NotAuthenticated,
#     ParseError,
#     PermissionDenied,
#     ValidationError,
# )
#
# from apps.pizza.models import PizzaModel

# def filter_pizza(query: QueryDict) -> QuerySet:
#     qs = PizzaModel.objects.all()
#
#     for k, v in query.items():
#         match k:
#             case 'price_gt':
#                 qs = qs.filter(price__gt=v)
#             case 'price_lt':
#                 qs = qs.filter(price__lt=v)
#             case _:
#                 raise ValidationError({'detail': f'"{k}" not allowed'})
#
#     return qs
from django_filters import rest_framework as filters

from apps.pizza.models import DaysChoices, PizzaModel


class PizzaFilter(filters.FilterSet):
    lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    range = filters.RangeFilter(field_name='size')  # range_min=2&range_max=100
    price_in = filters.BaseInFilter(field_name='price')  # price_in=30,25,2000
    day = filters.ChoiceFilter('day', choices=DaysChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            'id',
            'name',
            ('price', 'asd')
        )
    )  # order=name asc
    # order=-name desc

# PizzaModel.objects.filter(price__gt=0)
