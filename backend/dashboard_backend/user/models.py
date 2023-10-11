from django.db import models
from crypto.models import Crypto
from stock.models import Stock
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    salt = models.CharField(max_length=10)
    legal_name = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    stocks = models.ManyToManyField(Stock, "StockQuantity", blank=True)
    crypto = models.ManyToManyField(Crypto, "CryptoQuantity", blank=True)


class StockQuantity(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.DecimalField(decimal_places=2, max_digits=15)
    shares = models.IntegerField(validators=[MinValueValidator(0)])


class CryptoQuantity(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.DecimalField(decimal_places=2, max_digits=15)
    shares = models.IntegerField(validators=[MinValueValidator(0)])
