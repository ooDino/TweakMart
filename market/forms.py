from django import forms
from .models import Lot, Bid

class LotForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = ('name', 'description', 'startBid', 'image',)

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ('amount',)