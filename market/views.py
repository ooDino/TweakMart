from django.shortcuts import render, redirect 
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Lot
from .forms import LotForm

# Create your views here.
class MarketView(View):
    def get(self, request):
        context = {'lots': Lot.objects.all()}
        return render(request, 'market/market.html', context)

class MarketFormView(View):
    def get(self, request):
        form = LotForm()
        context = {'form': form}
        return render(request, 'market/addLot.html', context)

    def post(self, request):
        form = LotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/market')

            

def deleteLot(request, id):
    lot = Lot.objects.get(id = id)
    lot.delete()
    return redirect('/market')
