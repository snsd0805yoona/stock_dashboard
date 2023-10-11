from django.db import models


# Create your models here.
class Stock(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    marketPrice = models.DecimalField(decimal_places=2, max_digits=15)
    update_at = models.DateField(auto_now=True)


class StockRecord(models.Model):
    stock_code = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    volume = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
