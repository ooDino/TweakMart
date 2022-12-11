from django.shortcuts import render, redirect 
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Lot
from .forms import LotForm

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
