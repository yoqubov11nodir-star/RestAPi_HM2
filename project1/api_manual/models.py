from django.db import models

class Smartphone(models.Model):
    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    ram = models.IntegerField()
    storage = models.IntegerField()
    battery = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_5g = models.BooleanField(default=True)

    def __str__(self):
        return self.model_name