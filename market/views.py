from django.shortcuts import render, redirect 
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Lot, Bid
from .forms import LotForm, BidForm

# Create your views here.
class MarketView(View):
    def get(self, request):
        context = {'lots': Lot.objects.all(), 'loggedIn': request.user.is_authenticated}
        return render(request, 'market/market.html', context)

class MarketFormView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = LotForm()
            context = {'form': form}
            return render(request, 'market/addLot.html', context)
        else:
            return redirect('/accounts/login/')

    def post(self, request):
        if request.user.is_authenticated:
            form = LotForm(request.POST, request.FILES)
            if form.is_valid():
                lot = Lot()
                lot.name = request.POST['name']
                lot.description = request.POST['description']
                lot.startBid = request.POST['startBid']
                lot.image = request.FILES['image']
                lot.user = request.user
                lot.save()
                return redirect('/market')
        else:
            return redirect('/accounts/login/')

def deleteLot(request, id):
    lot = Lot.objects.get(id = id)
    lot.delete()
    return redirect('/market')

class BidFormView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            form = BidForm()
            context = {'form': form, 'id': id}
            return render(request, 'market/bid.html', context)
        else:
            return redirect('/accounts/login/')
    
    def post(self, request, id):
        if request.user.is_authenticated:
            form = BidForm(request.POST)
            if form.is_valid():
                bid = Bid()
                bid.lot = Lot.objects.get(id = id)
                bid.amount = request.POST['amount']
                bid.user = request.user
                bid.save()
                return redirect('/market')

        else:
            return redirect('/accounts/login/')

class LotView(View):
    def get(self, request, id):
        lot = Lot.objects.get(id = id)
        bids = lot.bid_set.all()
        context = {'lot': lot, 'bids': bids}
        return render(request, 'market/lot.html', context)
