from .views import MarketView, MarketFormView, deleteLot, BidFormView, LotView
from django.urls import path

urlpatterns = [
    path('', MarketView.as_view(), name="market"),
    path('lot/<int:id>', LotView.as_view(), name='lot'),
    path('addLot/', MarketFormView.as_view(), name="market-lot"),
    path('deleteLot/<int:id>', deleteLot , name="market-delete-lot"),
    path('bid/<int:id>', BidFormView.as_view(), name="market-bid")
]