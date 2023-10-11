from stock import models
from wallstreet import Stock as wallstreet_stock


def update_stock():
    stocks = models.Stock.objects.all()
    for stock in stocks:
        code = stock.code

        s = wallstreet_stock(code)

        stock.marketPrice = s.price
        stock.save()


# def create_stock_record(code, price, volume):
