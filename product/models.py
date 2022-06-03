from django.db import models


class DrinkModel(models.Model):
    class Meta:
        db_table = "Drink"

    name = models.CharField(max_length=256)
    category = models.ForeignKey("DrinkModel", on_delete=models.CASCADE)
    information = models.TextField(max_length=256)
    allergy = models.CharField(max_length=256)
