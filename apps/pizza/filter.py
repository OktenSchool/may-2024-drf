from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.pizza.models import PizzaModel


def filter_pizza(query: QueryDict) -> QuerySet:
    qs = PizzaModel.objects.all()

    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case _:
                raise ValidationError({'detail': f'"{k}" not allowed'})

    return qs
