from django.db import models


# Create your models here.
class Crypto(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    website = models.EmailField(max_length=50)


class CryptoRecord(models.Model):
    crypto_code = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    created_at = models.DateTimeField(auto_now_add=True)
