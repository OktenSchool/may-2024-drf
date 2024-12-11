from django.db import models

class UserModel(models.Model):
    class Meta:
        db_table = 'users'
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    status = models.BooleanField(default=False)
    weight = models.FloatField()

