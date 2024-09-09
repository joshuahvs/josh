from django.db import models

# Create your models here.
class joshShop(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()

    @property
    def is_price_expensive(self):
        return self.price > 1000000