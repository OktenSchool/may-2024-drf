# Generated by Django 5.1.4 on 2024-12-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_alter_pizzamodel_pizza_shop_alter_pizzamodel_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzamodel',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Tuesday', max_length=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizzamodel',
            name='size',
            field=models.IntegerField(),
        ),
    ]
