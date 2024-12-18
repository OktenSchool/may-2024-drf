from django.db import models


class PizzaShopModel(models.Model):
    class Meta:
        db_table = 'pizza_shops'

    name = models.CharField(max_length=100)