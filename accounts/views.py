from django.views.generic import CreateView, UpdateView
from .forms import CreateUserForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


class RegisterView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

def EditUserView(request):
    user = User.objects.get(id=request.user.id)
    user.username = request.POST['new_user']
    user.profile.phone_number = request.POST['new_number']
    user.profile.address = request.POST['new_address']
    
    user.save()
    return redirect(request.META.get('HTTP_REFERER'))

def EditPassword(request):
    user = User.objects.get(id=request.user.id)
    
    if check_password(request.POST['old_pass'], user.password):
        user.password = make_password(request.POST['new_pass'])
    user.save()
    return redirect(request.META.get('HTTP_REFERER'))

def AddCard(request):
    user = User.objects.get(id=request.user.id)
    user.profile.card_number = request.POST['cardnumber']
    user.profile.card_name = request.POST['cardname']
    user.profile.expire = request.POST['expire']
    user.profile.cvv = request.POST['cvv']
    
    user.save()
    return redirect(request.META.get('HTTP_REFERER'))

def Withdraw(request):
    user = User.objects.get(id=request.user.id)
    user.profile.bal = user.profile.bal - int(request.POST['withdraw_amount'])

    user.save()
    return redirect(request.META.get('HTTP_REFERER'))

def Deposit(request):
    user = User.objects.get(id=request.user.id)
    user.profile.bal = user.profile.bal + int(request.POST['deposit_amount'])

    user.save()
    return redirect(request.META.get('HTTP_REFERER'))