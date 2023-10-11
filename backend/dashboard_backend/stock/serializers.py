from rest_framework import serializers
from models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["code", "name", "website", "marketPrice", "updatedAt"]


class StockUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["marketPrice"]
