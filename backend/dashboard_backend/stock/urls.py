from django.urls import path

from stock import views

urlpatterns = [
    path("", views.StockListView.as_view(), name="list_stock"),
]
