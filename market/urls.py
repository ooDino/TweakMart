from .views import MarketView, MarketFormView, deleteLot
from django.urls import path

urlpatterns = [
    path('', MarketView.as_view(), name="market"),
    path('addLot/', MarketFormView.as_view(), name="market-lot"),
    path('deleteLot/<int:id>', deleteLot , name="market-delete-lot")
]