from django.core import validators as V
from django.db import models

from apps.pizza.managers import PizzaManager
from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.pizza_shop.models import PizzaShopModel
from core.services.file_service import upload_pizza_photo


class DaysChoices(models.TextChoices):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizzas'
        ordering = ('-id',)

    # name = models.CharField(max_length=20, blank=True)
    # name = models.CharField(max_length=20, blank=True)
    # size = models.IntegerField(default=25)
    # price = models.FloatField(null=True)
    # pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')
    name = models.CharField(max_length=20,validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)] )
    size = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(100)])
    price = models.FloatField()
    day = models.CharField(max_length=9, choices=DaysChoices.choices)
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')
    photo = models.ImageField(upload_to=upload_pizza_photo, blank=True)
    objects = PizzaManager()